from bisect import bisect
from functools import lru_cache
from typing import List


class Solution:
    """
    Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

    In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

    If there is no way to make arr1 strictly increasing, return -1.

    Example 1:

    Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
    Output: 1
    Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
    Example 2:

    Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
    Output: 2
    Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
    Example 3:

    Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
    Output: -1
    Explanation: You can't make arr1 strictly increasing.
    """
    def makeArrayIncreasing1(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1:0}
        arr2.sort()

        for num1 in arr1:
            new_dp = {}
            for key in dp:
                if num1 > key:
                    new_dp[num1] = min(new_dp.get(num1, float("inf")), dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    new_dp[arr2[loc]] = min(new_dp.get(arr2[loc], float("inf")), dp[key] + 1)
            dp = new_dp
        if dp:
            return min(dp.values())
        return -1
    
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m, n = len(arr1), len(arr2)
        arr2.sort()

        @lru_cache(None)
        def dfs(idx1, v2):
            if idx1 == m:
                return 0
            j = bisect.bisect_left(arr2, v2 + 1)
            return min(
                dfs(idx1 + 1, arr2[j]) + 1 if j < n else float("inf"),
                dfs(idx1 + 1, arr1[idx1]) if idx1 == 0 or arr1[idx1] > v2 else float("inf")
            ) 
        res = dfs(0, min(arr2) - 1)
        return res if res < float("inf") else -1