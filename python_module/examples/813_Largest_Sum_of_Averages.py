class Solution:
    """
    You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.

    Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

    Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.

    Example 1:

    Input: nums = [9,1,2,3,9], k = 3
    Output: 20.00000
    Explanation: 
    The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
    That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
    Example 2:

    Input: nums = [1,2,3,4,5,6,7], k = 4
    Output: 20.50000
    """
    def largestSumOfAverages1(self, nums: List[int], k: int) -> float:
        n = len(nums)

        @lru_cache(None)  # Memoization to avoid recomputation
        def helper(idx, p):
            if p == 1:  # Base case: Only one partition left
                return sum(nums[idx:]) / (n - idx)  # Take the remaining part

            max_score = float('-inf')
            curr_sum = 0  # Track sum for current partition

            for i in range(idx, n - k + 1):  # Ensure we have enough elements left for `k-1` partitions
                curr_sum += nums[i]  # Update sum of nums[i:j+1]
                avg = curr_sum / (i - idx + 1)  # Compute average of this partition
                max_score = max(max_score, avg + helper(i + 1, p - 1))  # Recurse for remaining partitions

            return max_score

        return helper(0, k)
    
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        if not nums:
            return -1

        n = len(nums)
        @cache
        def helper(idx: int, p: int):
            if p == 1:
                return sum(nums[idx:]) / (n - idx)
            
            cur_sum, max_avg = 0, float('-inf')
            for i in range(idx, n - p + 1):
                cur_sum += nums[i]
                avg = cur_sum / (i - idx + 1)
                max_avg = max(max_avg, avg + helper(i + 1, p - 1))
            return max_avg
        
        return helper(0, k)