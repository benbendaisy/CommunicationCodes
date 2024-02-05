class Solution:
    def minimumOneBitOperations1(self, n: int) -> int:
        if n == 0:
            return 0
        k = 0
        cur = 1
        while cur * 2 <= n:
            cur *= 2
            k += 1
        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations1(n ^ cur)

    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        k = 0
        mask = 1
        while mask <= n:
            if n & mask:
                res = 2 ** (k + 1) - 1 - res
            mask <<= 1
            k += 1
        return res