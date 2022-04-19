from collections import defaultdict
from typing import List


class Solution:
    def generatePermutations1(self, st: set, chars: list, candidate: list):
        if not chars:
            if candidate == candidate[::-1]:
                st.add("".join(candidate))
            return
        for i in range(len(chars)):
            candidate.append(chars[i])
            self.generatePermutations(st, chars[:i] + chars[i+1:], candidate)
            candidate.pop()

    def isPermutation(self, s: str):
        charMap = defaultdict(int)
        for ch in s:
            charMap[ch] += 1
        cnt = 0
        for key, value in charMap.items():
            if value % 2 != 0:
                cnt += 1
        return True if cnt < 2 else False


    def generatePermutations(self, st: set, chars: list, cur: int):
        length = len(chars)
        if cur == length:
            if chars == chars[::-1]:
                st.add("".join(chars))
            return

        for i in range(cur, length):
            if chars[i] != chars[cur] or i == cur:
                chars[cur], chars[i] = chars[i], chars[cur]
                self.generatePermutations(st, chars, cur + 1)
                chars[cur], chars[i] = chars[i], chars[cur]

    def generatePalindromes(self, s: str) -> List[str]:
        if not s or not self.isPermutation(s):
            return []

        chars = [x for x in s]
        st = set()
        self.generatePermutations(st, chars, 0)
        return list(st)

if __name__ == "__main__":
    s = "aabbhijkkjih"
    solution = Solution()
    ret = solution.generatePalindromes(s)
    print(ret)
