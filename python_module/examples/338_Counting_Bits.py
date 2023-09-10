from typing import List


class Solution:
    """
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

        Example 1:

        Input: n = 2
        Output: [0,1,1]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        Example 2:

        Input: n = 5
        Output: [0,1,1,2,1,2]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101

        Constraints:

        0 <= n <= 105

    """
    def countBits(self, n: int) -> List[int]:
        if n < 0:
            return []
        res = [0]
        def count_one(num):
            cnt = 0
            while num > 0:
                if num & 1 == 1:
                    cnt += 1
                num >>= 1
            return cnt
        for i in range(1, n + 1):
            cnt = count_one(i)
            res.append(cnt)
        return res