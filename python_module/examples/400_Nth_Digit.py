class Solution:
    """
        Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

        Example 1:

        Input: n = 3
        Output: 3
        Example 2:

        Input: n = 11
        Output: 0
        Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
    """
    def findNthDigit1(self, n: int) -> int:
        # returns the number of digits among numbers less than equal to num
        def count(num):
            k = len(str(num))
            cnt = 0
            for i in range(k - 1):
                cnt += 9 * (i + 1) * pow(10, i)
            cnt += (num - 10 ** (k - 1) + 1) * k
            return cnt

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1
        return int(str(left)[::-1][count(left) - n])

    def findNthDigit(self, n: int) -> int:
        """
            Math
            The problem can be break down into different group based on the digits, 1 - 9, 10 - 99, where the cnt is 9, 90, and etc
            Time complexity O(log n)
            Space complexity O(1)
        :param n:
        :return:
        """
        # refer to: https://just4once.gitbooks.io/leetcode-notes/content/leetcode/math/400-nth-digit.html
        length = 1
        cnt = 9
        start = 1
        while n > length * cnt:
            n -= length * cnt
            cnt *= 10
            start *= 10
            length += 1
        start += (n - 1) // length
        return int(str(start)[(n - 1) % length])


