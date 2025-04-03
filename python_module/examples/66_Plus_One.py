from typing import List


class Solution:
    """
        You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

        Increment the large integer by one and return the resulting array of digits.

        Example 1:

        Input: digits = [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
        Incrementing by one gives 123 + 1 = 124.
        Thus, the result should be [1,2,4].
        Example 2:

        Input: digits = [4,3,2,1]
        Output: [4,3,2,2]
        Explanation: The array represents the integer 4321.
        Incrementing by one gives 4321 + 1 = 4322.
        Thus, the result should be [4,3,2,2].
        Example 3:

        Input: digits = [9]
        Output: [1,0]
        Explanation: The array represents the integer 9.
        Incrementing by one gives 9 + 1 = 10.
        Thus, the result should be [1,0].
    """
    def plusOne1(self, digits: List[int]) -> List[int]:
        if not digits:
            return []

        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            digit = (carry + digits[i]) % 10
            carry = (carry + digits[i]) // 10
            digits[i] = digit
        if carry != 0:
            digits.insert(0, carry)
        return digits
    
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        
        res, n = [], len(digits)
        carrier = 1
        for digit in digits[::-1]:
            value = digit + carrier
            carrier = value // 10
            res.append(value % 10)
        
        if carrier > 0:
            res.append(carrier)
        return res[::-1]