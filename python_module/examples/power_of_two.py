class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return false
        k = n
        while k % 2 == 0:
            k /= 2
        return true if k == 1 else false