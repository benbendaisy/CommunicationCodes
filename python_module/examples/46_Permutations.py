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
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def permutation(idx: int):
            if idx == n:
                res.append(nums[:])
                return
            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                permutation(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
        permutation(0)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back_track(path, choices):
            if not choices:
                res.append(path)
                return
            for i in range(len(choices)):
                back_track(path + [choices[i]], choices[:i] + choices[i + 1:])
        back_track([], nums)
        return res
