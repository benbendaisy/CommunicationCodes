class Solution:
    def isPalindrome1(self, s: str) -> bool:
        if not s:
            return False
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        if not s:
            return False
        chars = [x for x in s.lower() if x.isalnum()]
        l, r = 0, len(chars) - 1
        while l < r:
            if chars[l] != chars[r]:
                return False
            l, r = l + 1, r - 1

        return True
    
    def isPalindrome(self, s: str) -> bool:
        char_list = [ch.lower() for ch in s if (ch.isalpha() or ch.isnumeric())]
        s1 = "".join(char_list)
        return s1 == s1[::-1]
