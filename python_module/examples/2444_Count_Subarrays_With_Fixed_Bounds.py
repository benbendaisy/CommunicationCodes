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
    def countSubarrays1(self, nums: List[int], minK: int, maxK: int) -> int:
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

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # min_position, max_position: the MOST RECENT positions of minK and maxK.
        # left_bound: the MOST RECENT value outside the range [minK, maxK].
        res = 0
        min_pos = max_pos = left_bound = -1
        # Iterate over nums, for each number at index i:
        for i, num in enumerate(nums):
            # If the number is outside the range [minK, maxK], update the most recent left_bound.
            if num < minK or num > maxK:
                left_bound = i
            # If the number is minK or maxK, update the most recent position.
            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i
            # The number of valid subarrays equals the number of elements between left_bound and 
            # the smaller of the two most recent positions.
            res += max(0, min(min_pos, max_pos) - left_bound)
        return res