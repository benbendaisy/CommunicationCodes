class Solution:
    """
    Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

    Example 1:

    Input: n = 20
    Output: 1
    Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
    Example 2:

    Input: n = 100
    Output: 10
    Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
    Example 3:

    Input: n = 1000
    Output: 262
    """
    def numDupDigitsAtMostN(self, n: int) -> int:
        def is_special(m: int) -> bool:
            digits = list(map(int, str(m)))
            mask = 0
            for num in digits:
                if mask & (1 << num) != 0:
                    return True
                mask |= 1 << num
            return False
        
        cnt = 0
        for i in range(1, n + 1):
            if is_special(i):
                cnt += 1
        return cnt