class Solution:
    """
        Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

        The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

        Return the quotient after dividing dividend by divisor.

        Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

        Example 1:

        Input: dividend = 10, divisor = 3
        Output: 3
        Explanation: 10/3 = 3.33333.. which is truncated to 3.
        Example 2:

        Input: dividend = 7, divisor = -3
        Output: -2
        Explanation: 7/-3 = -2.33333.. which is truncated to -2.

        Constraints:

        -231 <= dividend, divisor <= 231 - 1
        divisor != 0
    """
    def divide(self, dividend: int, divisor: int) -> int:
        """
            Steps

                Initially, set the answer variable i.e. the quotient to 0.
                
                Check if any one of the numbers is negative and store it in a separate variable.

                Make both the numbers positive.

                Start from n = 31 the most significant bit and loop till n = 0 the least significant bit.

                Check if shifting the divisor by n bits is less than or equal to the dividend

                if so subtract it from the dividend and update the dividend
                Add 2 power n to the answer
                ( Note: Here the dividend is reduced to the reminder each time the condition is true. )

                And finally, return the quotient after checking if it should be positive or negative with the result from step 2.
        :param dividend:
        :param divisor:
        :return:
        """
        isNegative = False
        if dividend < 0:
            dividend = -dividend
            isNegative = ~isNegative

        if divisor < 0:
            divisor = -divisor
            isNegative = ~isNegative

        maxInt = 2**31 - 1
        minInt = -2**31

        res = 0
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                res += 1 << i
        if isNegative:
            res = -res

        if res >= maxInt:
            return maxInt
        elif res <= minInt:
            return minInt

        return res