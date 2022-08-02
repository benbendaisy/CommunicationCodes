from typing import List


class Solution:
    """
        Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:

        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
        Example 2:

        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]
        Example 3:

        Input: nums = [], target = 0
        Output: [-1,-1]

        Constraints:

        0 <= nums.length <= 105
        -109 <= nums[i] <= 109
        nums is a non-decreasing array.
        -109 <= target <= 109
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l)//2
            if nums[m] == target:
                idxL = idxR = m
                while idxL >= 0 and nums[idxL] == target:
                    idxL -= 1
                while idxR < len(nums) and nums[idxR] == target:
                    idxR += 1
                if idxL < 0 or nums[idxL] != target:
                    idxL += 1
                if idxR == len(nums) or nums[idxR] != target:
                    idxR -= 1
                return [idxL, idxR]
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [-1, -1]
