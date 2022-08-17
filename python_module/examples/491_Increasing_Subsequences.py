from typing import List


class Solution:
    """
        Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.

        The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.

        Example 1:

        Input: nums = [4,6,7,7]
        Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
        Example 2:

        Input: nums = [4,4,3,2,1]
        Output: [[4,4]]

        Constraints:

        1 <= nums.length <= 15
        -100 <= nums[i] <= 100
    """
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 0

        res, visited = [], set()

        def dfs(idx, sub, prev):
            if len(sub) > 1:
                temp = tuple(sub)
                if temp not in visited:
                    res.append(sub.copy())
                visited.add(temp)

            if idx == len(nums):
                return

            if nums[idx] >= prev:
                dfs(idx + 1, sub + [nums[idx]], nums[idx])

            dfs(idx + 1, sub, prev)

        dfs(0, [], -10000)

        return res
