import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.distributions import Categorical
import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
GAMMA = 0.99                # Discount factor
LEARNING_RATE_ACTOR = 0.0003
LEARNING_RATE_CRITIC = 0.001
PPO_EPSILON = 0.2           # Clipping parameter for PPO
PPO_EPOCHS = 10             # Number of epochs to update policy per batch
PPO_BATCH_SIZE_TRAJ = 2048  # Number of timesteps to collect in each batch/rollout
# PPO_MINIBATCH_SIZE = 64 # Minibatch size for updates (can be implemented for larger PPO_BATCH_SIZE_TRAJ)
# For simplicity in this example, we'll update on the whole trajectory batch
GAE_LAMBDA = 0.95           # Lambda for Generalized Advantage Estimation
ENTROPY_COEF = 0.01         # Entropy bonus coefficient
MAX_EPISODES = 600
MAX_STEPS_PER_EPISODE = 500
SOLVED_THRESHOLD = 475

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Actor Network
class Actor(nn.Module):
    def __init__(self, state_size, action_size):
        super(Actor, self).__init__()
        self.fc1 = nn.Linear(state_size, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc_policy = nn.Linear(128, action_size) # Outputs logits for actions

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        action_logits = self.fc_policy(x)
        return F.softmax(action_logits, dim=-1) # Probabilities

# Critic Network
class Critic(nn.Module):
    def __init__(self, state_size):
        super(Critic, self).__init__()
        self.fc1 = nn.Linear(state_size, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc_value = nn.Linear(128, 1) # Outputs state value

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        value = self.fc_value(x)
        return value

# PPO Agent
class PPOAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.actor = Actor(state_size, action_size).to(device)
        self.critic = Critic(state_size).to(device)

        self.optimizer_actor = optim.Adam(self.actor.parameters(), lr=LEARNING_RATE_ACTOR)
        self.optimizer_critic = optim.Adam(self.critic.parameters(), lr=LEARNING_RATE_CRITIC)

        # Temporary storage for trajectories
        self.memory = [] # Will store (state, action, reward, next_state, done, log_prob)

    def store_transition(self, state, action, reward, next_state, done, log_prob):
        self.memory.append((state, action, reward, next_state, done, log_prob))

    def clear_memory(self):
        self.memory = []

    def select_action(self, state):
        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(device)
        with torch.no_grad():
            action_probs = self.actor(state_tensor)
        dist = Categorical(action_probs)
        action = dist.sample()
        log_prob = dist.log_prob(action)
        return action.item(), log_prob.item()

    def compute_advantages_and_returns(self, rewards, dones, values, next_values):
        advantages = np.zeros_like(rewards, dtype=np.float32)
        returns = np.zeros_like(rewards, dtype=np.float32)
        gae = 0
        # Ensure next_values is a numpy array if it's a tensor
        if isinstance(next_values, torch.Tensor):
            next_values = next_values.cpu().numpy().flatten()


        for t in reversed(range(len(rewards))):
            delta = rewards[t] + GAMMA * next_values[t] * (1 - dones[t]) - values[t]
            gae = delta + GAMMA * GAE_LAMBDA * (1 - dones[t]) * gae
            advantages[t] = gae
            returns[t] = gae + values[t] # GAE is A_t, so A_t + V(s_t) = Q_t (which is our return target)

        # Normalize advantages
        advantages = (advantages - np.mean(advantages)) / (np.std(advantages) + 1e-8)
        return torch.FloatTensor(advantages).to(device), torch.FloatTensor(returns).to(device)


    def learn(self):
        if not self.memory:
            return

        # Unpack memory
        states, actions, rewards, next_states, dones, old_log_probs = zip(*self.memory)

        states_np = np.array(states, dtype=np.float32)
        actions_np = np.array(actions, dtype=np.int64)
        rewards_np = np.array(rewards, dtype=np.float32)
        next_states_np = np.array(next_states, dtype=np.float32)
        dones_np = np.array(dones, dtype=np.bool_)
        old_log_probs_np = np.array(old_log_probs, dtype=np.float32)

        # Convert to tensors
        states_tensor = torch.FloatTensor(states_np).to(device)
        actions_tensor = torch.LongTensor(actions_np).to(device)
        # rewards_tensor = torch.FloatTensor(rewards_np).to(device) # Not directly used in loss like this
        # dones_tensor = torch.BoolTensor(dones_np).to(device)
        old_log_probs_tensor = torch.FloatTensor(old_log_probs_np).to(device)

        # Calculate advantages and returns (value targets)
        with torch.no_grad():
            values = self.critic(states_tensor).squeeze().cpu().numpy()
            # Need value of the very last next_state for GAE calculation
            # If the last state was terminal, its next_value is 0
            last_next_state_tensor = torch.FloatTensor(next_states_np[-1]).unsqueeze(0).to(device)
            last_done = dones_np[-1]
            next_value_of_last_state = self.critic(last_next_state_tensor).item() if not last_done else 0.0

            # Create next_values array for GAE
            # For non-terminal states, it's V(s_{t+1}). For terminal, it's 0.
            next_values_for_gae = np.zeros(len(rewards_np), dtype=np.float32)
            next_state_values_critic = self.critic(torch.FloatTensor(next_states_np).to(device)).squeeze().cpu().numpy()

            for i in range(len(rewards_np)):
                if dones_np[i]:
                    next_values_for_gae[i] = 0.0
                else:
                    next_values_for_gae[i] = next_state_values_critic[i]


        advantages, returns_tensor = self.compute_advantages_and_returns(rewards_np, dones_np, values, next_values_for_gae)
        advantages = advantages.unsqueeze(1) # Match shape for multiplication
        returns_tensor = returns_tensor.unsqueeze(1)


        # PPO Update Loop (multiple epochs)
        for _ in range(PPO_EPOCHS):
            # Actor (Policy) Loss
            action_probs_current = self.actor(states_tensor)
            dist_current = Categorical(action_probs_current)
            current_log_probs = dist_current.log_prob(actions_tensor)
            entropy = dist_current.entropy().mean() # For entropy bonus

            # Ratio of probabilities: pi_theta / pi_theta_old
            ratios = torch.exp(current_log_probs - old_log_probs_tensor) # old_log_probs are detached
            ratios = ratios.unsqueeze(1) # Ensure ratios have shape [batch_size, 1]

            surr1 = ratios * advantages
            surr2 = torch.clamp(ratios, 1 - PPO_EPSILON, 1 + PPO_EPSILON) * advantages
            actor_loss = -torch.min(surr1, surr2).mean() - ENTROPY_COEF * entropy

            self.optimizer_actor.zero_grad()
            actor_loss.backward()
            # nn.utils.clip_grad_norm_(self.actor.parameters(), 0.5) # Optional gradient clipping
            self.optimizer_actor.step()

            # Critic (Value) Loss
            current_values = self.critic(states_tensor) # Shape [batch_size, 1]
            critic_loss = F.mse_loss(current_values, returns_tensor)

            self.optimizer_critic.zero_grad()
            critic_loss.backward()
            # nn.utils.clip_grad_norm_(self.critic.parameters(), 0.5) # Optional gradient clipping
            self.optimizer_critic.step()

        self.clear_memory() # Clear memory after updates

# Training Loop
if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    agent = PPOAgent(state_size, action_size)
    episode_rewards = []
    total_timesteps = 0

    print(f"Starting training on {device}...")
    print(f"State size: {state_size}, Action size: {action_size}")

    for episode in range(1, MAX_EPISODES + 1):
        state, _ = env.reset()
        episode_reward = 0
        
        # PPO collects a batch of trajectories before updating
        # This inner loop is for collecting PPO_BATCH_SIZE_TRAJ timesteps
        # Note: This might span across multiple episodes if PPO_BATCH_SIZE_TRAJ is large
        
        # For simplicity, in this example, we will make one PPO update per episode,
        # collecting up to MAX_STEPS_PER_EPISODE or PPO_BATCH_SIZE_TRAJ, whichever is smaller
        # A more standard PPO implementation collects PPO_BATCH_SIZE_TRAJ timesteps, which might
        # be across several episodes, then updates.
        
        current_episode_timesteps = 0
        for step in range(MAX_STEPS_PER_EPISODE):
            action, log_prob = agent.select_action(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            
            agent.store_transition(state, action, reward, next_state, done, log_prob)
            
            state = next_state
            episode_reward += reward
            total_timesteps += 1
            current_episode_timesteps +=1

            if done or current_episode_timesteps >= PPO_BATCH_SIZE_TRAJ : # Simplified: update after each episode or if batch full
                # Perform PPO update
                agent.learn() # This clears memory internally
                if done: # if done, the episode ends, otherwise continue collecting for this "rollout"
                    break
        
        episode_rewards.append(episode_reward)

        if episode % 10 == 0:
            avg_reward = np.mean(episode_rewards[-100:])
            print(f"Episode: {episode}/{MAX_EPISODES}, Total Timesteps: {total_timesteps}, Avg Reward (last 100): {avg_reward:.2f}, Last Reward: {episode_reward:.2f}")

        if len(episode_rewards) >= 100:
            if np.mean(episode_rewards[-100:]) >= SOLVED_THRESHOLD:
                print(f"\nEnvironment solved in {episode} episodes! Total timesteps: {total_timesteps}")
                print(f"Average reward over the last 100 episodes: {np.mean(episode_rewards[-100:]):.2f}")
                # torch.save(agent.actor.state_dict(), 'ppo_actor_cartpole_solved.pth')
                # torch.save(agent.critic.state_dict(), 'ppo_critic_cartpole_solved.pth')
                break
    
    if episode == MAX_EPISODES and np.mean(episode_rewards[-100:]) < SOLVED_THRESHOLD:
         print("\nTraining finished. Environment not solved within the episode limit.")
         print(f"Final average reward over the last 100 episodes: {np.mean(episode_rewards[-100:]):.2f}")

    env.close()

    # Plotting results
    plt.figure(figsize=(12, 6))
    plt.plot(episode_rewards, label='Episode Reward')
    if len(episode_rewards) >= 100:
        rolling_avg = np.convolve(episode_rewards, np.ones(100)/100, mode='valid')
        plt.plot(np.arange(99, len(episode_rewards)), rolling_avg, label='100-episode rolling average', color='red')
    plt.title('Episode Rewards Over Time (PPO)')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.legend()
    plt.grid(True)
    plt.show()