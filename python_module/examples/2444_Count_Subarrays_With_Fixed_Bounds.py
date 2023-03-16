from typing import List


class Solution:
    """
        You are given an integer array nums and two integers minK and maxK.

        A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

        The minimum value in the subarray is equal to minK.
        The maximum value in the subarray is equal to maxK.
        Return the number of fixed-bound subarrays.

        A subarray is a contiguous part of an array.



        Example 1:

        Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
        Output: 2
        Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
        Example 2:

        Input: nums = [1,1,1,1], minK = 1, maxK = 1
        Output: 10
        Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
    """
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        left = -1
        last_min, last_max = -1, -1
        cnt = 0
        for i in range(n):
            if nums[i] >= minK and nums[i] <= maxK:
                last_min = i if nums[i] == minK else last_min
                last_max = i if nums[i] == maxK else last_max
                cnt += max(0, min(last_min, last_max) - left)
            else:
                left = i
                last_min, last_max = -1, -1
        return cnt