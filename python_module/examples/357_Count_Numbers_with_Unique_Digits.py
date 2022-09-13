class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def f(k):
            if k == 0: return 1
            res, cur = 9, 9
            while k > 1:
                res *= cur
                cur -= 1
                k -= 1
            return res
        res = 0
        for i in range(n+1):
            res += f(i)
        return res