class Solution:

    def __init__(self):
        self.cnt = 0

    def countSubstrings1(self, s: str) -> int:
        if not s:
            return 0
        cnt = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                subStr = s[i:j]
                if subStr == subStr[::-1]:
                    cnt += 1
        return cnt
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def count_palindrome(low, high):
            res = 0
            while low >= 0 and high < n:
                if s[low] != s[high]:
                    break
                low -= 1
                high += 1
                res += 1
            return res
        res = 0
        for i in range(n):
            res += count_palindrome(i, i)
            res += count_palindrome(i, i + 1)
        return res

if __name__ == "__main__":
    s = "abc"
    solution = Solution()
    ret = solution.countSubstrings(s)
    print(ret)