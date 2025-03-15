from functools import lru_cache


class Solution:
    @lru_cache(None)
    def fib1(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
    
    @cache
    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
    
    def fib(self, n: int) -> int:
        @cache
        def helper(m: int) -> int:
            if m == 0: return 0
            if m == 1: return 1
            return helper(m - 1) + helper(m - 2)
        
        return helper(n)