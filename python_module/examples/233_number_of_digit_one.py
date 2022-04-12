class Solution:
    def countDigitOne(self, n: int) -> int:
        if not n:
            return 0

        cnt = 0
        for i in range(n + 1):
            cnt += str(i).count("1")

        return cnt