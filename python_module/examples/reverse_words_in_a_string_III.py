class Solution:
    def reverseWord(self, s: list, left: int, right: int):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        l = r = 0
        string = [ch for ch in s]
        while r < len(string):
            while r < len(string) and string[r] != ' ':
                r += 1
            self.reverseWord(string, l, r - 1)
            r += 1
            l = r
        return "".join(string)
if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    solution = Solution()
    ret = solution.reverseWords(s)
    print(ret)