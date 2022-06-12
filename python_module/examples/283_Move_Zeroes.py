from typing import List


class Solution:
    """
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Example 1:

        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        Example 2:

        Input: nums = [0]
        Output: [0]

        Constraints:

        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        idx1 = idx2 = 0

        while idx1 < len(nums):
            while idx2 < len(nums) and nums[idx2] != 0:
                idx2 += 1

            idx1 = idx2
            while idx1 < len(nums) and nums[idx1] == 0:
                idx1 += 1
            if idx1 < len(nums):
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    solution = Solution()
    ret = solution.moveZeroes(nums)
    print(nums)

