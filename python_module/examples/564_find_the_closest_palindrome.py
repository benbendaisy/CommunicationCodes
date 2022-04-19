class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if not n:
            return n
        left, right = int(n) - 1, int(n) + 1
        while left >= 0:
            str1 = str(left)
            if str1 == str1[::-1]:
                return str1
            str2 = str(right)
            if str2 == str2[::-1]:
                return str2
            left, right = left - 1, right + 1
        return None