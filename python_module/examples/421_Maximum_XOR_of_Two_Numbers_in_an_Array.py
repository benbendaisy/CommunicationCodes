import math
from typing import List


class Solution:
    """
        Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

        Example 1:

        Input: nums = [3,10,5,25,2,8]
        Output: 28
        Explanation: The maximum result is 5 XOR 25 = 28.
        Example 2:

        Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
        Output: 127
    """
    def findMaximumXOR1(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        n = len(nums)
        xor = -math.inf
        for i in range(n - 1):
            for j in range(i + 1, n):
                xor = max(xor, nums[i]^nums[j])
        return xor

    def findMaximumXOR(self, nums: List[int]) -> int:
        # length of max number in a binary representation
        n = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(n)[::-1]:
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            cur_xor = max_xor | 1
            # compute all existing prefixes
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= any(cur_xor^p in prefixes for p in prefixes)
        return max_xor


