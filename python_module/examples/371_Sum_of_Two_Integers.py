class Solution:
    """
        Given two integers a and b, return the sum of the two integers without using the operators + and -.

        Example 1:

        Input: a = 1, b = 2
        Output: 3
        Example 2:

        Input: a = 2, b = 3
        Output: 5

        Constraints:

        -1000 <= a, b <= 1000
    """
    def getSum1(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)
    
    def getSum(a, b):
        # 32-bit mask to handle overflow
        mask = 0xFFFFFFFF
        
        # Iterate until there is no carry
        while b != 0:
            # Calculate the sum without considering the carry (using XOR)
            sum_without_carry = (a ^ b) & mask
            # Calculate the carry (using AND and left shift)
            carry = ((a & b) << 1) & mask
            # Update a and b for the next iteration
            a = sum_without_carry
            b = carry
        
        # Handle negative numbers (if a is negative in 32 bits)
        if a > 0x7FFFFFFF:  # If the result is negative in 32 bits
            a = ~(a ^ mask)  # Convert to negative number in Python's representation
        return a