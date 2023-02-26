from typing import List


class Solution:
    """
        The array-form of an integer num is an array representing its digits in left to right order.

        For example, for num = 1321, the array form is [1,3,2,1].
        Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

        Example 1:

        Input: num = [1,2,0,0], k = 34
        Output: [1,2,3,4]
        Explanation: 1200 + 34 = 1234
        Example 2:

        Input: num = [2,7,4], k = 181
        Output: [4,5,5]
        Explanation: 274 + 181 = 455
        Example 3:

        Input: num = [2,1,5], k = 806
        Output: [1,0,2,1]
        Explanation: 215 + 806 = 1021
    """
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_k = str(k)
        ln, lk = len(num) - 1, len(str_k) - 1
        res = []
        carry = 0
        while ln >= 0 or lk >= 0 or carry:
            total = carry
            if ln >= 0:
                total += num[ln]
                ln -= 1
            if lk >= 0:
                total += int(str_k[lk])
                lk -= 1
            res.insert(0, total % 10)
            carry = total // 10
        return res

