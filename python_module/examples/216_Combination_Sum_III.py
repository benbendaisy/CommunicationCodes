from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []

        res = []
        def combinations(m: int, idx: int, arr: list):
            if m == 0:
                if sum(arr) == n: # check if sum of the arr equals target n
                    res.append(arr)
                return

            for i in range(idx + 1, 10): # only consider the nums that are less than 10
                sums = sum(arr)
                if sums + i <= n: # only consider the valid num
                    combinations(m - 1, i, arr + [i])

        combinations(k, 0, [])
        return res
