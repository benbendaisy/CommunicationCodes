from typing import List


class Solution:
    """
        Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

        Example 1:

        Input: nums = [4,6,7,7]
        Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
        Example 2:

        Input: nums = [4,4,3,2,1]
        Output: [[4,4]]
    """
    def findSubsequences1(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = set()
        n = len(nums)
        for bitmask in range(1, 1 << n):
            # build the sequence
            sequence = [nums[i] for i in range(n) if (bitmask >> i) & 1]
            # check if its length is at least 2, and it is increasing
            if len(sequence) > 1 and all([sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1)]):
                res.add(tuple(sequence))
        return res

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        def dfs(idx, sub, prev_num):
            if len(sub) > 1:
                res.add(tuple(sub))
            if idx == n:
                return
            if nums[idx] >= prev_num:
                dfs(idx + 1, sub + [nums[idx]], nums[idx])
            dfs(idx + 1, sub, prev_num)
        dfs(0, [], -10000)
        return res


