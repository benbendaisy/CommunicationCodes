from collections import defaultdict
from typing import List


class Solution:
    """
        Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

        An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

        Example 1:

        Input: nums = [23,2,4,6,7], k = 6
        Output: true
        Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
        Example 2:

        Input: nums = [23,2,6,4,7], k = 6
        Output: true
        Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
        42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
        Example 3:

        Input: nums = [23,2,6,4,7], k = 13
        Output: false
    """
    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        n = len(nums)
        for i in range(n):
            sums = nums[i]
            for j in range(i + 1, n):
                sums += nums[j]
                if sums % k == 0:
                    return True
        return False

    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        # initialize the hash map with index 0 for sum 0
        if len(nums) < 2:
            return False

        n = len(nums)
        hashMap = {0:0}
        sums = 0
        for i in range(n):
            sums += nums[i]
            # if the remainder s % k occurs for the first time
            if sums % k not in hashMap:
                hashMap[sums % k] = i + 1
            # if the subarray size is at least twice
            elif hashMap[sums % k] < i:
                return True
        return False
    
    def checkSubarraySum3(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        running_sum = 0
        positions = {0:0}
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            if remainder not in positions:
                positions[remainder] = i + 1
            elif positions[remainder] < i:
                return True
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        prefix_sum = 0
        # To handle cases where prefix sum itself is a multiple of k
        position_dict = {0:-1}

        for i, v in enumerate(nums):
            prefix_sum += v
            remainder = prefix_sum % k
            # Store first occurrence of remainder
            if remainder not in position_dict:
                position_dict[remainder] = i
            else:
                # Ensure subarray length >= 2
                if i - position_dict[remainder] > 1:
                    return True
        return False
