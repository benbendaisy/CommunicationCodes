class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        k = n
        while k % 2 == 0:
            k /= 2
        return True if k == 1 else False