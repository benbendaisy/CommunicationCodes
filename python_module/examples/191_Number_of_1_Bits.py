class Solution:
    """
        Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

        Note:

        Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
        In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

        Example 1:

        Input: n = 00000000000000000000000000001011
        Output: 3
        Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
        Example 2:

        Input: n = 00000000000000000000000010000000
        Output: 1
        Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
        Example 3:

        Input: n = 11111111111111111111111111111101
        Output: 31
        Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

        Constraints:

        The input must be a binary string of length 32.
    """
    def hammingWeight1(self, n: int) -> int:
        cnt = 0
        while n > 0:
            if n & 1 == 1:
                cnt += 1
            n >>= 1
        return cnt
    
    def hammingWeight2(self, n: int) -> int:
        cnt = 0
        while n != 0:
            cnt += 1
            n &= (n - 1)
        return cnt
    
    def hammingWeight3(self, n: int) -> int:
        cnt = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                cnt += 1
            mask <<= 1
        return cnt
    
    def hammingWeight4(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt
    
    def hammingWeight5(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt