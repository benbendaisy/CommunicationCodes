class Solution:
    """
    Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.
 
    Example 1:

    Input: n = 5
    Output: 5
    Explanation:
    Here are the non-negative integers <= 5 with their corresponding binary representations:
    0 : 0
    1 : 1
    2 : 10
    3 : 11
    4 : 100
    5 : 101
    Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
    Example 2:

    Input: n = 1
    Output: 2
    Example 3:

    Input: n = 2
    Output: 3
    """
    def countDigitOne1(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        count = 1
        while n >= 10:
            count += str(n).count('1')
            n -= 1
        return count
    
    def findIntegers(self, n: int) -> int:
        count = 0
        factor = 1  # Represents ones, tens, hundreds place, etc.

        while factor <= n:
            higher = n // (factor * 10)  # Digits left of the current place
            lower = n % factor  # Digits right of the current place
            digit = (n // factor) % 10  # Current digit at factor place
            
            if digit == 0:
                count += higher * factor
            elif digit == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor

            factor *= 10  # Move to the next place
        
        return count