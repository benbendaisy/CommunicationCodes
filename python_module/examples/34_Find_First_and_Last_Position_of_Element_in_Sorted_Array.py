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
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                lidx, ridx = mid, mid
                while lidx >= 0 and nums[lidx] == target:
                    lidx -= 1
                while ridx < n and nums[ridx] == target:
                    ridx += 1
                return [lidx + 1, ridx - 1]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1, -1]
