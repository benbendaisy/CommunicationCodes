class Solution:
    """
    You are given an array nums consisting of positive integers.

    We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

    Return the length of the longest nice subarray.

    A subarray is a contiguous part of an array.

    Note that subarrays of length 1 are always considered nice.

    Example 1:

    Input: nums = [1,3,8,48,10]
    Output: 3
    Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
    - 3 AND 8 = 0.
    - 3 AND 48 = 0.
    - 8 AND 48 = 0.
    It can be proven that no longer nice subarray can be obtained, so we return 3.
    Example 2:

    Input: nums = [3,1,5,11,13]
    Output: 1
    Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
    """
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left, max_len, bit_mask = 0, 0, 0

        for right in range(len(nums)):
            while (bit_mask & nums[right]) != 0:
                bit_mask ^= nums[left]  # Remove nums[left] from the bitmask
                left += 1
            bit_mask |= nums[right]  # Add nums[right] to the bitmask
            max_len = max(max_len, right - left + 1)

        return max_len
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        Not working for all test cases
        """
        if not nums:
            return 0
        
        left, right, n = 0, 1, len(nums)
        max_and = 1
        for right in range(1, n):
            while left < right and ((nums[left] & nums[right]) != 0):
                left += 1
            max_and = max(max_and, right - left + 1)
        return max_and