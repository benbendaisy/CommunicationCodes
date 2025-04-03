class Solution:
    """
    Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

    Example 1:

    Input: left = 5, right = 7
    Output: 4
    Example 2:

    Input: left = 0, right = 0
    Output: 0
    Example 3:

    Input: left = 1, right = 2147483647
    Output: 0
    

    Constraints:

    0 <= left <= right <= 231 - 1
    """
    def rangeBitwiseAnd1(self, left: int, right: int) -> int:
         # Keep track of how many right shifts we perform
        shift = 0
        
        # Keep right shifting both numbers until they become equal
        # This helps us find the common prefix of both numbers
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Left shift the number back by the number of shifts we performed
        # This gives us the bitwise AND of the entire range
        return left << shift
    
    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        """
        Alternative implementation using Brian Kernighan's algorithm.
        Keeps turning off the rightmost 1-bit of right until it's <= left.
        """
        while right > left:
            # Turn off the rightmost 1-bit
            right = right & (right - 1)
        return right
    
    def rangeBitwiseAnd3(self, left: int, right: int) -> int:
        """
        Time Limit Exceeded for large ranges.
        """
        res = left
        for num in range(left + 1, right + 1):
            res &= num
        return res