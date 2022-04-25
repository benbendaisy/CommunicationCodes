class Solution:
    def checkPalindromeFormation1(self, a: str, b: str) -> bool:
        def checkPalindrome(str1: str, str2: str) -> bool:
            if not str1:
                return False
            length = len(str1)
            for i in range(length):
                mergedStr1 = str1[:i] + str2[i:]
                if mergedStr1 == mergedStr1[::-1]:
                    return True
            return False

        return checkPalindrome(a, b) or checkPalindrome(b, a)

    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def checkPalindrome(a: str, b: str):
            l, r = 0, len(b) - 1
            while l < r and a[l] == b[r]:
                l += 1
                r -= 1
            str1 = a[:l] + b[l + 1:]
            str2 = a[:r] + b[r + 1:]
            return str1 == str1[::-1] or str2 == str2[::-1]

        return checkPalindrome(a, b)
