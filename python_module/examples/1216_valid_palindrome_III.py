from typing import List


class Solution:
    def checkPalindrome(self, chars: list, k):
        if chars == chars[::-1]:
            return True
        elif k <= 0:
            return False

        for i in range(len(chars)):
            if self.checkPalindrome(chars[:i] + chars[i + 1:], k - 1):
                return True

        return False

    def validPalindrome(self, s: str, memory: List[List[int]], left: int, right: int) -> int:
        if left >= right:
            return 0
        if left == right - 1:
            return 0 if s[left] == s[right] else 1
        if memory[left][right] != -1:
            return memory[left][right]

        if s[left] == s[right]:
            memory[left][right] = self.validPalindrome(s, memory, left + 1, right - 1)
        else:
            memory[left][right] = 1 + min(self.validPalindrome(s, memory, left + 1, right), self.validPalindrome(s, memory, left, right - 1))
        return memory[left][right]

    def isValidPalindrome2(self, s: str, k: int) -> bool:
        """
        top down
        :param s:
        :param k:
        :return:
        """
        length = len(s)
        memory = [[-1] * length for x in range(length)]
        return self.validPalindrome(s, memory, 0, length - 1) <= k

    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        bottom up
        :param s:
        :param k:
        :return:
        """
        length = len(s)
        memory = [[0] * length for i in range(length)]
        for i in range(0, length, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    memory[i][j] = memory[i + 1][j - 1]
                else:
                    memory[i][j] = 1 + min(memory[i + 1][j], memory[i][j - 1])

        return memory[0][length - 1] <= k


    def isValidPalindrome1(self, s: str, k: int) -> bool:
        if not s:
            return False

        chars = [x for x in s]
        return self.checkPalindrome(chars, k)

if __name__ == "__main__":
    s = "daabbddbdaadcabbccdddabaabadadadacaababdabdbaaccadadbbadaacbbbdd"
    k = 4
    solution = Solution()
    ret = solution.isValidPalindrome2(s, k)
    print(ret)