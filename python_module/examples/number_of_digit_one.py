class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        count = 1
        while n >= 10:
            count += str(n).count('1')
            n -= 1
        return count