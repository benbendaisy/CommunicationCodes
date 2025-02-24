from functools import lru_cache


class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
    
    @cache
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)