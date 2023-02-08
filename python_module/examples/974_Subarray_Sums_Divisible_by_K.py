from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    """
        Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

        A subarray is a contiguous part of an array.

        Example 1:

        Input: nums = [4,5,0,-2,-3,1], k = 5
        Output: 7
        Explanation: There are 7 subarrays with a sum divisible by k = 5:
        [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
        Example 2:

        Input: nums = [5], k = 9
        Output: 0
    """
    def subarraysDivByK_1(self, nums: List[int], k: int) -> int:
        def can_be_divised_by_k(arr: List[int]) -> bool:
            return sum(arr) % k == 0

        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if can_be_divised_by_k(nums[i:j]):
                    res += 1
        return res

    def subarraysDivByK2(self, nums: List[int], k: int) -> int:
        m, res = [1] + [0 for i in range(k - 1)], 0
        for i in accumulate(nums):
            res += m[i % k]
            m[i % k] += 1
        return res

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        nums_dict = defaultdict(int)
        nums_dict[0] = 1
        res = 0
        accumulate_sum = 0
        for num in nums:
            accumulate_sum += num
            remainder = accumulate_sum % k
            res += nums_dict[remainder]
            nums_dict[remainder] += 1
        return res

