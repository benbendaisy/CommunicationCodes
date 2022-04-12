class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s

        reversed_string = s[::-1]
        for i in range(0, len(s)):
            if s[: len(s) - i] == reversed_string[i:]:
                return reversed_string[:i] + s

        return ""

if __name__ == "__main__":
    s = "aacecaaa"
    solution = Solution()
    ret = solution.shortestPalindrome(s)
    print(ret)