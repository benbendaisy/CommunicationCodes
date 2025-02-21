class Solution:
    """
    An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

    Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

    Example 1:

    Input: n = 10
    Output: 9
    Example 2:

    Input: n = 1234
    Output: 1234
    Example 3:

    Input: n = 332
    Output: 299
    """
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        marker = length
        for i in range(length - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i
        for i in range(marker, length):
            digits[i] = '9'
        return int("".join(digits))