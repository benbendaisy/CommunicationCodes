class Solution:
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
    frequency
    of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

    Example 1:

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
    Example 2:

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
    Example 3:

    Input: candidates = [2], target = 1
    Output: []
    """
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        def back_track(path: list[int], idx: int):
            if sum(path) == target:
                res.append(path)
                return
            elif sum(path) > target:
                return
            for i in range(idx, len(candidates)):
                back_track(path + [candidates[i]], i)
        back_track([], 0)
        return res
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        n = len(candidates)
        res = []
        def helper(path: list, idx: int):
            if sum(path) == target:
                res.append(path)
                return

            if idx >= n:
                return
            
            for i in range(idx, n):
                path_sum = sum(path)
                if path_sum + candidates[i] <= target:
                    helper(path + [candidates[i]], i)
        helper([], 0)
        return res
    
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return 0
        
        res, n = [], len(candidates)
        def helper(idx: int, running_sum: int, path: list):
            if running_sum == target:
                res.append(path)
                return
            if running_sum > target or idx > n:
                return
            
            for i in range(idx, n):
                helper(i, running_sum + candidates[i], path + [candidates[i]])
        helper(0, 0, [])
        return res
    
    def combinationSum4(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        n, res = len(candidates), []

        @cache
        def helper(idx: int, path: tuple):
            path_sum = sum(path)
            if path_sum == target:
                res.append(list(path))
                return
                    
            if idx == n:
                return
            
            for i in range(idx, n):
                if candidates[i] + path_sum <= target:
                    helper(i, path + (candidates[i],))
        helper(0, ())
        return res