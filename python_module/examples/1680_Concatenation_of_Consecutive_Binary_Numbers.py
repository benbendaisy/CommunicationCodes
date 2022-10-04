class Solution:
    """
        Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

        Example 1:

        Input: n = 1
        Output: 1
        Explanation: "1" in binary corresponds to the decimal value 1.
        Example 2:

        Input: n = 3
        Output: 27
        Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
        After concatenating them, we have "11011", which corresponds to the decimal value 27.
        Example 3:

        Input: n = 12
        Output: 505379714
        Explanation: The concatenation results in "1101110010111011110001001101010111100".
        The decimal value of that is 118505380540.
        After modulo 109 + 7, the result is 505379714.


        Constraints:

        1 <= n <= 105
    """
    def concatenatedBinary1(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        concatenation = "".join([bin(i)[2:] for i in range(n + 1)])
        return int(concatenation, 2) % MOD

    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        length, res = 0, 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                length += 1
            print((res << length))
            res = ((res << length) | i) % MOD
        return res

if __name__ == "__main__":
    n = 5
    solution = Solution()
    ret = solution.concatenatedBinary(n)
    print(ret)
