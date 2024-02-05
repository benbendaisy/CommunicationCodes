from typing import List


class Solution:
    """
        Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

        We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

        Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

        Example 1:

        Input: arr = [2,4]
        Output: 3
        Explanation: We can make these trees: [2], [4], [4, 2, 2]
        Example 2:

        Input: arr = [2,4,5,10]
        Output: 7
        Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

        Constraints:

        1 <= arr.length <= 1000
        2 <= arr[i] <= 109
        All the values of arr are unique.
    """
    def numFactoredBinaryTrees1(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        arr.sort()
        dp = [1] * n
        indexMap = {v:i for i, v in enumerate(arr)}
        for i, v in enumerate(arr):
            for j in range(i):
                if v % arr[j] == 0:
                    rightValue = v / arr[j]
                    if rightValue in indexMap:
                        dp[i] += dp[j] * dp[indexMap[rightValue]]
                        dp[i] %= MOD

        return sum(dp) % MOD

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        arr.sort()
        dp = [1] * n
        indexes = {x:i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                # arr[j] will be left child
                if x % arr[j] == 0:
                    right = x / arr[j]
                    if right in indexes:
                        dp[i] += dp[j] * dp[indexes[right]]
                        dp[i] %= mod
        return sum(dp) % mod