class Solution:
    """
    The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

    For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
    Given an integer n, return its complement.

    Example 1:

    Input: n = 5
    Output: 2
    Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
    """
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
         # Find the number of bits required to represent n
        num_bits = n.bit_length()

        # Create a mask with 1's in all positions up to the highest bit of n
        mask = (1 << num_bits) - 1
        
        # Flip the bits of n using XOR with the mask
        return n ^ mask