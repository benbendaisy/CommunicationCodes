from functools import lru_cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
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