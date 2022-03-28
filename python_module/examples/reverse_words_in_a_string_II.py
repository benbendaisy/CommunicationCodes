from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return

        l = r = 0
        while r < len(s):
            while r < len(s) and s[r] != ' ':
                r += 1
            self.reverseWord(s, l, r - 1)
            # skip all empty space
            # while r < len(s) and s[r] != ' ':
            #     r += 1
            l = r + 1
            r += 1
        self.reverseWord(s, 0, len(s) - 1)

    def reverseWord(self, s, l, r) -> None:
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == "__main__":
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    solution = Solution()
    ret = solution.reverseWords(s)
    print(s)








