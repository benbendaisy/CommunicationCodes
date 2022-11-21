from collections import Counter


class Solution:
    """
        Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

        Example 1:

        Input: s = "owoztneoer"
        Output: "012"
        Example 2:

        Input: s = "fviefuro"
        Output: "45"
    """
    def originalDigits(self, s: str) -> str:
        digits = [
            [0, 'z', []],
            [2, 'w', []],
            [4, 'u', []],
            [6, 'x', []],
            [8, 'g', []],
            [5, 'f', [4]],
            [7, 's', [6]],
            [3, 'h', [8]],
            [9, 'i', [6, 8, 5]],
            [1, 'o', [0, 2, 4]]
        ]
        fmap, ans, n = [0] * 26, [0] * 10, len(s)
        for i in range(10):
            digit, char, rems = digits[i]
            cnt = s.count(char)
            for rem in rems:
                cnt -= ans[rem]
            ans[digit] += cnt
        return "".join([str(i) * ans[i] for i in range(10)])
