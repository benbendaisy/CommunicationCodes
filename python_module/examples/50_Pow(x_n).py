from functools import lru_cache


class Solution:
    def myPow1(self, x: float, n: int) -> float:
        @lru_cache(None)
        def helper(k):
            if k == 0:
                return 1
            res = helper(k // 2)
            res = res * res
            if k % 2 == 0:
                return res

            return res * x
        if x == 0:
            return 0
        res = helper(abs(n))
        if n >= 0:
            return res
        else:
            return 1 / res
        
    def myPow(self, x: float, n: int) -> float:
        @cache
        def helper(m: int):
            if m == 0:
                return 1
            res = helper(m // 2)
            res = res * res
            if m % 2 == 0:
                return res
            return res * x
        res = helper(abs(n))
        if n > 0:
            return res
        return 1 / res