from typing import List


class Solution:
    """
        Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

        You may assume the input array always has a valid answer.

        Example 1:

        Input: nums = [3,5,2,1,6,4]
        Output: [3,5,1,6,2,4]
        Explanation: [1,6,2,5,3,4] is also accepted.
        Example 2:

        Input: nums = [6,6,5,6,3,8]
        Output: [6,6,5,6,3,8]

        Constraints:

        1 <= nums.length <= 5 * 104
        0 <= nums[i] <= 104
        It is guaranteed that there will be an answer for the given input nums.
    """
    def wiggleSort1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i + 1], nums[i] = nums[i], nums[i + 1]

    def wiggleSort2(self, nums: List[int]) -> None:
        less = True
        for i in range(len(nums) - 1):
            if less:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            less = not less

    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

if __name__ == "__main__":
    solution = Solution()
    nums = [3,5,2,1,6,4]
    ret = solution.wiggleSort2(nums)
    print(ret)
