class Solution:
    """
        Given an integer n, return true if it is a power of four. Otherwise, return false.

        An integer n is a power of four, if there exists an integer x such that n == 4x.

        Example 1:

        Input: n = 16
        Output: true
        Example 2:

        Input: n = 5
        Output: false
        Example 3:

        Input: n = 1
        Output: true
    """
    def isPowerOfFour1(self, n: int) -> bool:
        if n < 0:
            return False

        while n % 4 == 0 and n > 0:
            n >>= 2
        return n == 1

    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False

        while n % 4 == 0 and n > 3:
            n >>= 2

        return n == 1
if __name__ == "__main__":
    solution = Solution()
    ret = solution.isPowerOfFour(16)
    print(ret)