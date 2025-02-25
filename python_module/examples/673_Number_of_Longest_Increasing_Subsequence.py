from typing import List


class Solution:
    """
    Given an integer array nums, return the number of longest increasing subsequences.

    Notice that the sequence has to be strictly increasing.

    Example 1:

    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
    Example 2:

    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
    """
    def findNumberOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        longest_len = max(dp)
        return sum([count[i] for i in range(n) if dp[i] == longest_len])
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        Find the number of longest increasing subsequences in a given array.
        
        Args:
            nums: List of integers
            
        Returns:
            The number of longest increasing subsequences
        """
        if not nums:
            return 0
            
        n = len(nums)
        
        # lengths[i] = length of longest increasing subsequence ending at nums[i]
        lengths = [1] * n
        
        # counts[i] = number of longest increasing subsequences ending at nums[i]
        counts = [1] * n
        
        # Compute lengths and counts
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # If we can extend the subsequence ending at j
                    if lengths[j] + 1 > lengths[i]:
                        # Found a longer subsequence
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        # Found another subsequence of the same length
                        counts[i] += counts[j]
        
        # Find the length of the longest increasing subsequence
        max_length = max(lengths)
        
        # Count all subsequences with the max length
        result = 0
        for i in range(n):
            if lengths[i] == max_length:
                result += counts[i]
                
        return result