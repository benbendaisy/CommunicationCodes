from typing import List


class Solution:
    """
    Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

    A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

    Example 1:

    Input: arr = [1,2,3,4], difference = 1
    Output: 4
    Explanation: The longest arithmetic subsequence is [1,2,3,4].
    Example 2:

    Input: arr = [1,3,5,7], difference = 1
    Output: 1
    Explanation: The longest arithmetic subsequence is any single element.
    Example 3:

    Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
    Output: 4
    Explanation: The longest arithmetic subsequence is [7,5,3,1].
    """
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        @lru_cache(None)
        def helper(index, prev):
            if index >= n:
                return 0
            take, nottake = 0, 0
            if prev == -10000:
                nottake = helper(index + 1, prev)
                take = 1 + helper(index + 1, arr[index])
            else:
                nottake = helper(index + 1, prev)
                if arr[index] - prev == difference:
                    take = 1 + helper(index + 1, arr[index])
            return max(take, nottake)
        return helper(0, -10000)
    
    def longestSubsequence1(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {} # Stores the maximum length at each index
        ans = 1 # Initialize with the minimum length of 1
        for i in range(n):
            num = arr[i]
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
            ans = max(ans, dp[num])
        return ans
