import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import random
import collections
import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
GAMMA = 0.99            # Discount factor for future rewards
EPSILON_START = 1.0     # Starting exploration rate
EPSILON_END = 0.01      # Minimum exploration rate
EPSILON_DECAY = 0.995   # Decay rate for exploration probability
LEARNING_RATE = 0.001   # Learning rate for the optimizer
BATCH_SIZE = 64         # Number of experiences sampled from the replay buffer
REPLAY_BUFFER_SIZE = 10000 # Maximum size of the replay buffer
TARGET_UPDATE_FREQ = 10 # How often to update the target network (in episodes)
MAX_EPISODES = 500      # Total number of episodes to train for
MAX_STEPS_PER_EPISODE = 500 # Max steps an agent can take in an episode for CartPole-v1

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 1. Q-Network (Model)
class QNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, action_size)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        return self.fc3(x)

# 2. Replay Buffer
class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = collections.deque(maxlen=capacity)

    def add(self, state, action, reward, next_state, done):
        experience = (state, action, reward, next_state, done)
        self.buffer.append(experience)

    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        return np.array(states, dtype=np.float32), \
               np.array(actions, dtype=np.int64), \
               np.array(rewards, dtype=np.float32), \
               np.array(next_states, dtype=np.float32), \
               np.array(dones, dtype=np.bool_)


    def __len__(self):
        return len(self.buffer)

# 3. DQN Agent
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.policy_net = QNetwork(state_size, action_size).to(device)
        self.target_net = QNetwork(state_size, action_size).to(device)
        self.target_net.load_state_dict(self.policy_net.state_dict()) # Initialize target_net with policy_net weights
        self.target_net.eval()  # Target network is not trained directly

        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=LEARNING_RATE)
        self.replay_buffer = ReplayBuffer(REPLAY_BUFFER_SIZE)
        self.epsilon = EPSILON_START

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randrange(self.action_size)  # Explore
        else:
            with torch.no_grad(): # No gradient needed for action selection
                state_tensor = torch.FloatTensor(state).unsqueeze(0).to(device)
                q_values = self.policy_net(state_tensor)
                return q_values.argmax().item() # Exploit: choose action with highest Q-value

    def learn(self):
        if len(self.replay_buffer) < BATCH_SIZE:
            return # Not enough samples to learn

        states, actions, rewards, next_states, dones = self.replay_buffer.sample(BATCH_SIZE)

        states_tensor = torch.FloatTensor(states).to(device)
        actions_tensor = torch.LongTensor(actions).unsqueeze(1).to(device) # Shape: (batch_size, 1)
        rewards_tensor = torch.FloatTensor(rewards).unsqueeze(1).to(device) # Shape: (batch_size, 1)
        next_states_tensor = torch.FloatTensor(next_states).to(device)
        dones_tensor = torch.BoolTensor(dones).unsqueeze(1).to(device) # Shape: (batch_size, 1)

        # Get Q-values for current states from policy_net
        # We want Q(s,a) for the actions that were actually taken
        current_q_values = self.policy_net(states_tensor).gather(1, actions_tensor)

        # Get Q-values for next states from target_net
        # We want max_a' Q_target(s', a')
        with torch.no_grad(): # Target network computations don't need gradients
            next_q_values_target = self.target_net(next_states_tensor).max(1)[0].unsqueeze(1)

        # Compute target Q-values: R + gamma * max_a' Q_target(s', a')
        # If s' is terminal, then the target is just R
        target_q_values = rewards_tensor + (GAMMA * next_q_values_target * (~dones_tensor))

        # Compute loss (Mean Squared Error)
        loss = F.mse_loss(current_q_values, target_q_values)

        # Optimize the model
        self.optimizer.zero_grad()
        loss.backward()
        # Gradient clipping (optional, but can help stability)
        # for param in self.policy_net.parameters():
        #     param.grad.data.clamp_(-1, 1)
        self.optimizer.step()

        # Decay epsilon
        self.epsilon = max(EPSILON_END, self.epsilon * EPSILON_DECAY)

    def update_target_network(self):
        self.target_net.load_state_dict(self.policy_net.state_dict())

# 4. Training Loop
if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    agent = DQNAgent(state_size, action_size)
    episode_rewards = []
    solved_threshold = 475 # CartPole-v1 is considered solved if average reward over 100 episodes is >= 475

    print(f"Starting training on {device}...")
    
    print(f"State size: {state_size}, Action size: {action_size}")

    for episode in range(1, MAX_EPISODES + 1):
        state, _ = env.reset()
        total_reward = 0

        for step in range(MAX_STEPS_PER_EPISODE):
            action = agent.select_action(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            agent.replay_buffer.add(state, action, reward, next_state, done)
            agent.learn() # Learn after each step if buffer is sufficiently full

            state = next_state
            total_reward += reward

            if done:
                break

        episode_rewards.append(total_reward)

        if episode % TARGET_UPDATE_FREQ == 0:
            agent.update_target_network()
            # print(f"Target network updated at episode {episode}")

        if episode % 10 == 0: # Log progress
            avg_reward = np.mean(episode_rewards[-100:]) # Average reward of the last 100 episodes
            print(f"Episode: {episode}/{MAX_EPISODES}, Total Reward: {total_reward:.2f}, Epsilon: {agent.epsilon:.3f}, Avg Reward (last 100): {avg_reward:.2f}")

        # Check for solving condition
        if len(episode_rewards) >= 100:
            if np.mean(episode_rewards[-100:]) >= solved_threshold:
                print(f"\nEnvironment solved in {episode} episodes!")
                print(f"Average reward over the last 100 episodes: {np.mean(episode_rewards[-100:]):.2f}")
                # Save the model (optional)
                # torch.save(agent.policy_net.state_dict(), 'dqn_cartpole_solved.pth')
                break
    
    if np.mean(episode_rewards[-100:]) < solved_threshold:
        print("\nTraining finished. Environment not solved within the episode limit.")
        print(f"Final average reward over the last 100 episodes: {np.mean(episode_rewards[-100:]):.2f}")


    env.close()

    # Plotting results
    plt.figure(figsize=(10, 5))
    plt.plot(episode_rewards)
    plt.title('Episode Rewards Over Time')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    # Add a rolling mean
    if len(episode_rewards) >= 100:
        rolling_avg = np.convolve(episode_rewards, np.ones(100)/100, mode='valid')
        plt.plot(np.arange(99, len(episode_rewards)), rolling_avg, label='100-episode rolling average')
        plt.legend()
    plt.grid(True)
    plt.show()