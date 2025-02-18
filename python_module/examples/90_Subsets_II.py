class Solution:
    """
    Given an integer array nums that may contain duplicates, return all possible 
    subsets
    (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

    Example 1:

    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    Example 2:

    Input: nums = [0]
    Output: [[],[0]]
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        res = [[]]
        def back_track(path: list, idx: int):
            if path:
                path.sort()
                res.append(path)
            if idx == m:
                return
            for i in range(idx, m):
                back_track(path + [nums[i]], i + 1)
        back_track([], 0)
        return list(map(list, {tuple(lst) for lst in res}))