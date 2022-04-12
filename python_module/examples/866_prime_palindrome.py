class Solution:
    def checkPrime(self, n: int) -> bool:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    def checkpalindrome(self, n: int):
        s = str(n)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
        return True

    def primePalindrome(self, n: int) -> int:
        if n == 1:
            n += 1
        while True:
            if self.checkPrime(n) and str(n) == str(n)[::-1]:
                return n
            n += 1