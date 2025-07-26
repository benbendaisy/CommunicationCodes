class Solution:
    """
    You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

    The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

    Return the maximum number of matchings between players and trainers that satisfy these conditions.

    Example 1:

    Input: players = [4,7,9], trainers = [8,2,5,8]
    Output: 2
    Explanation:
    One of the ways we can form two matchings is as follows:
    - players[0] can be matched with trainers[0] since 4 <= 8.
    - players[1] can be matched with trainers[3] since 7 <= 8.
    It can be proven that 2 is the maximum number of matchings that can be formed.
    Example 2:

    Input: players = [1,1,1], trainers = [10]
    Output: 1
    Explanation:
    The trainer can be matched with any of the 3 players.
    Each player can only be matched with one trainer, so the maximum answer is 1.
    """
    def matchPlayersAndTrainers1(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i = j = count = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1

        return count
    
    def matchPlayersAndTrainers2(self, players: List[int], trainers: List[int]) -> int:
        if not players or not trainers:
            return 0
        
        players.sort()
        trainers.sort()
        m, n = len(trainers), len(players)
        idx_t, idx_p, cnt = 0, 0, 0
        while idx_t < m and idx_p < n:
            while idx_t < m and players[idx_p] > trainers[idx_t]:
                idx_t += 1
            if idx_t < m:
                cnt += 1
            idx_p += 1
            idx_t += 1
        return cnt