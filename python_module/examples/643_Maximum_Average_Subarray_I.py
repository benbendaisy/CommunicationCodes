from typing import List


class Solution:
    """
    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

    Example 1:

    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    Example 2:

    Input: nums = [5], k = 1
    Output: 5.00000
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 0:
            return 0
        l, r = 0, 0
        sub_sums = 0
        for i in range(k):
            sub_sums += nums[i]
        r = k
        max_sum = sub_sums
        while r < len(nums):
            sub_sums += nums[r] - nums[l]
            max_sum = max(max_sum, sub_sums)
            r += 1
            l += 1
        return max_sum / k
        