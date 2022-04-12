import functools


class Solution:
    def validPalindrome(self, s: str) -> bool:
        @functools.lru_cache(None)
        def checkPalindrome(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False

                left, right = left + 1, right - 1
            return True

        if not s:
            return False
        elif checkPalindrome(0, len(s) - 1):
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return checkPalindrome(l, r - 1) or checkPalindrome(l + 1, r)

            l, r = l + 1, r - 1

        return True

if __name__ == "__main__":
    s = "cxcaac"
    solution = Solution()
    ret = solution.validPalindrome(s)
    print(ret)