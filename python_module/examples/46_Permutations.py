from typing import List


class Solution:
    """
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

        Example 1:

        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        Example 2:

        Input: nums = [0,1]
        Output: [[0,1],[1,0]]
        Example 3:

        Input: nums = [1]
        Output: [[1]]

        Constraints:

        1 <= nums.length <= 6
        -10 <= nums[i] <= 10
        All the integers of nums are unique.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutations(idx: int):
            if idx == len(nums):
                res.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                permutations(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        permutations(0)
        return res
