class Solution:

    def __init__(self):
        self.cnt = 0

    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        cnt = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                subStr = s[i:j]
                if subStr == subStr[::-1]:
                    cnt += 1
        return cnt

if __name__ == "__main__":
    s = "abc"
    solution = Solution()
    ret = solution.countSubstrings1(s)
    print(ret)