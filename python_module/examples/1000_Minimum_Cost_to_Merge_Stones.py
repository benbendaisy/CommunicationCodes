class Solution:
    """
    There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

    A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

    Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.can

    Example 1:

    Input: stones = [3,2,4,1], k = 2
    Output: 20
    Explanation: We start with [3, 2, 4, 1].
    We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
    We merge [4, 1] for a cost of 5, and we are left with [5, 5].
    We merge [5, 5] for a cost of 10, and we are left with [10].
    The total cost was 20, and this is the minimum possible.
    Example 2:

    Input: stones = [3,2,4,1], k = 3
    Output: -1
    Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
    Example 3:

    Input: stones = [3,5,1,2,6], k = 3
    Output: 25
    Explanation: We start with [3, 5, 1, 2, 6].
    We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
    We merge [3, 8, 6] for a cost of 17, and we are left with [17].
    The total cost was 25, and this is the minimum possible.
    """
    def mergeStones1(self, stones: List[int], k: int) -> int:
        n = len(stones)
    
        # If it's impossible to merge all piles into one, return -1
        if (n - 1) % (k - 1) != 0:
            return -1
        
        # Precompute prefix sums for efficient range sum calculation
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        @lru_cache(maxsize=None)
        def helper(left: int, right: int) -> int:
            if right - left + 1 < k:
                return 0  # No cost if no merging is possible
            
            res = float('inf')
            
            # Try all possible splits where we can merge k consecutive piles
            for mid in range(left, right, k - 1):
                res = min(res, helper(left, mid) + helper(mid + 1, right))
            
            # If the current segment can be merged into one pile, add the sum of the segment
            if (right - left) % (k - 1) == 0:
                res += prefix_sum[right + 1] - prefix_sum[left]
            
            return res
        
        return helper(0, n - 1)
    
    def mergeStones2(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1  # If merging to one pile is impossible
        
        prefix = [0] + list(accumulate(stones))  # Prefix sum for quick range sum lookup
        
        @cache
        def helper(i, j, piles):
            if (j - i + 1 - piles) % (k - 1) != 0:
                return float('inf')  # Invalid state
            if i == j:
                return 0 if piles == 1 else float('inf')  # Base case
            
            if piles == 1:
                return helper(i, j, k) + prefix[j + 1] - prefix[i]  # Merge k piles into 1
            
            # Try merging into `piles` piles
            return min(helper(i, m, 1) + helper(m + 1, j, piles - 1) for m in range(i, j, k - 1))
        
        return helper(0, n - 1, 1)
    

    def mergeStones3(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1  # If merging to one pile is impossible
        
        prefix = [0] + list(accumulate(stones))  # Prefix sum for quick range sum lookup
        
        @cache
        def helper(i, j, piles):
            if i == j:
                return 0 if piles == 1 else float('inf')  # Base case
            
            if piles == 1:
                return helper(i, j, k) + prefix[j + 1] - prefix[i]  # Merge k piles into 1
            
            # Try merging into `piles` piles
            return min(helper(i, m, 1) + helper(m + 1, j, piles - 1) for m in range(i, j, k - 1))
        
        return helper(0, n - 1, 1)