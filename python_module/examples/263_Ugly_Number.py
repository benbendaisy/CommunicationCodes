class Solution:
    """
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.

    Example 1:

    Input: n = 6
    Output: true
    Explanation: 6 = 2 × 3
    Example 2:

    Input: n = 1
    Output: true
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
    Example 3:

    Input: n = 14
    Output: false
    Explanation: 14 is not ugly since it includes the prime factor 7.

    Constraints:

    -231 <= n <= 231 - 1
    """
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n = n / i
            if n == 1:
                return True

        return False