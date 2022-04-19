from typing import List


class Solution:
    maxCut = 1000
    def countPalindromeDistance(self, s: str):
        left, right = 0, len(s) - 1
        cnt = 0
        while left < right:
            if s[left] != s[right]:
                cnt += 1
            left, right = left + 1, right - 1
        return cnt

    def palindromePartitions(self, s: str, memory: List[List], left: int, k: int):
        length = len(s)
        # valid case
        if left >= length and k == 0:
            return 0
        elif left >= length:
            return 1e3
        # invalid case
        if k == 0:
            return 1e3

        if memory[left][k] >= 0:
            return memory[left][k]

        memory[left][k] = 1e3
        for i in range(left + 1, length + 1):
            cost = self.countPalindromeDistance(s[left:i])
            memory[left][k] = min(memory[left][k], cost + self.palindromePartitions(s, memory, i, k - 1))
        return memory[left][k]


    def palindromePartition(self, s: str, k: int) -> int:
        length = len(s)
        if length == k:
            return 0
        elif length < k:
            return -1
        memory = [[-1] * (k + 1) for x in range(length + 1)]
        return self.palindromePartitions(s, memory, 0, k)

if __name__ == "__main__":
    s = "aabbc"
    solution = Solution()
    ret = solution.palindromePartition(s, 3)
    print(ret)