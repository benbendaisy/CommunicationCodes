from typing import List


class Solution:
    """
    Given an integer array nums of unique elements, return all possible 
    subsets
    (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

    Example 1:

    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Example 2:

    Input: nums = [0]
    Output: [[],[0]]
    """
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        def dfs(idx, sub_set):
            for i in range(idx, n):
                sub_set.append(nums[i])
                res.append(sub_set[:])
                dfs(i + 1, sub_set)
                sub_set.pop()
        dfs(0, [])
        return res
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        def back_track(path: list, idx: int):
            if path:
                path.sort()
                res.append(path)
            if idx == n:
                return
            for i in range(idx, n):
                back_track(path + [nums[i]], i + 1)
        
        back_track([], 0)

        return res
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        res = [[]]

        def back_track(path: List[int], idx: int):
            if path:
                res.append(path)
            if idx == m:
                return
            for i in range(idx, m):
                back_track(path + [nums[i]], i + 1)
        back_track([], 0)
        return res