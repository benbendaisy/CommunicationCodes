class Solution:
    def checkPartions(self, s: str, cur: int, k: int):
        length = len(s)
        if cur >= length:
            return False
        elif k == 0:
            substr = s[cur:]
            if substr == substr[::-1]:
                return True
            return False

        for i in range(cur + 1, length):
            sub = s[cur:i]
            if sub == sub[::-1] and self.checkPartions(s, i, k - 1):
                return True
        return False

    def checkPartitioning(self, s: str) -> bool:
        if len(s) < 3:
            return False
        elif len(s) == 3:
            return True

        return self.checkPartions(s, 0, 3)

if __name__ == "__main__":
    s = "bcbddxy"
    solution = Solution()
    ret = solution.checkPartitioning(s)
    print(ret)