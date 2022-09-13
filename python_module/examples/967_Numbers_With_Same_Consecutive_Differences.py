from typing import List


class Solution:
    """
        Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

        Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

        You may return the answer in any order.

        Example 1:

        Input: n = 3, k = 7
        Output: [181,292,707,818,929]
        Explanation: Note that 070 is not a valid number, because it has leading zeroes.
        Example 2:

        Input: n = 2, k = 1
        Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

        Constraints:

        2 <= n <= 9
        0 <= k <= 9
    """
    def numsSameConsecDiff1(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        ans = []
        def dfs(m, num):
            if m == 0:
                return ans.append(num)

            tailDigit = num % 10
            nextDigits = set([tailDigit - k, tailDigit + k])
            for digit in nextDigits:
                if 0 <= digit < 10:
                    newNum = num * 10 + digit
                    dfs(m - 1, newNum)

        for num in range(1, 10):
            dfs(n - 1, num)

        return ans

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        queue = [i for i in range(1, 10)]
        if n == 1:
            return [0] + queue

        for level in range(n - 1):
            newQueue = []
            for num in queue:
                tailDigit = num % 10
                nextDigits = set([tailDigit - k, tailDigit + k])
                for digit in nextDigits:
                    if 0 <= digit < 10:
                        newNum = num * 10 + digit
                        newQueue.append(newNum)
            queue = newQueue

        return queue
