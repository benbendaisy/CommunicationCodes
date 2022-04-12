from typing import List


class Solution:

    def minimumMoves(self, arr: List[int]) -> int:
        l = len(arr)
        dp = [[0] * l for i in range(l + 1)]

        for left in range(l - 1, -1, -1):
            for right in range(left + 1, l):
                minMoves = right - left + 1
                if arr[left] == arr[right]:
                    minMoves = min(minMoves, dp[left + 1][right - 1])
                for i in range(left, right):
                    minMoves = min(minMoves, 1 + dp[left][i] + dp[i + 1][right])
                dp[left][right] = minMoves

        return 1 + dp[0][l - 1]

    def minimumMoves1(self, arr: List[int]) -> int:
        dp = [[-1] * len(arr) for i in range(len(arr))]
        return 1 + self.minMoves(arr, dp, 0, len(arr) - 1)

    def minMoves(self, arr: List[int], dp: List[List[int]], left: int, right: int):
        if left >= right:
            return 0
        elif dp[left][right] > 0:
            return dp[left][right]

        minMoves = right - left + 1
        if arr[left] == arr[right]:
            minMoves = min(minMoves, self.minMoves(arr, dp, left + 1, right - 1))

        for i in range(left, right):
            minMoves = min(minMoves, 1 + self.minMoves(arr, dp, left, i) + self.minMoves(arr, dp, i + 1, right))

        dp[left][right] = minMoves
        return minMoves


    def checkPalidrome(self, lst: List[int]):
        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def minimumMoves2(self, arr: List[int]) -> int:
        if not arr:
            return 0
        elif len(arr) == 1 or self.checkPalidrome(arr):
            return 1

        minMax = len(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if self.checkPalidrome(arr[i:j]):
                    minMax = min(minMax, self.minimumMoves(arr[:i] + arr[j:]))
        return 1 + minMax

if __name__ == "__main__":
    arr = [16,2,18,16,13,8,7,18,9,14,19,20,1,5,13,15,2,14,7,14,20,15,9,15,10,16,16,2,4,15,20,15,10,2,2,2,2,5,6,1,1,8,7,17,12,10,19,12,3,16,19,8,18,10,3,9,13,8,16,4,20,12,15,14,12,20,19,19,13,7,4,18,17,12,13,13,19,13,8,7,10,14,10,13,20,2,2,16,11,17,10,11,7,18,14,5,6,7,12,6]
    solution = Solution()
    ret = solution.minimumMoves1(arr)
    print(ret)