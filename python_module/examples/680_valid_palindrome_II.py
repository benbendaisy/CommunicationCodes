import functools


class Solution:
    def validPalindrome1(self, s: str) -> bool:
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
    
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, h = 0, len(s) - 1
        c = 0
        while l < h:
            t1, t2 = s[l], s[h]
            if t1 == t2:
                l += 1
                h -= 1
            else:
                temp1 = s[0: l] + s[l + 1:]
                temp2 = s[0:h] + s[h + 1:]
                if temp1 == temp1[::-1]:
                    return True
                elif temp2 == temp2[::-1]:
                    return True
                else:
                    return False
        return True

if __name__ == "__main__":
    s = "cxcaac"
    solution = Solution()
    ret = solution.validPalindrome(s)
    print(ret)