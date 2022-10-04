class Solution:
    """
        You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

        Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
        Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
        Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
        Given the integer n, return the last number that remains in arr.

        Example 1:

        Input: n = 9
        Output: 6
        Explanation:
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr = [2, 4, 6, 8]
        arr = [2, 6]
        arr = [6]
        Example 2:

        Input: n = 1
        Output: 1

        Constraints:

        1 <= n <= 109
    """
    def lastRemaining1(self, n: int) -> int:
        if n == 1:
            return 1
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))

    def lastRemaining(self, n: int) -> int:
        # since in first step we eliminate all odds so,
        #[1,2,3,4] --> [2,4]
        #[1,2,3,4,5] --> [2,4]
        # 1. f(2n+1) == f(2n)

        #after first elemination using left we left with even nums i.e 2*odd
        #[1,2,3,4,5,6,7,8,9,10] --> [2,4,6,8,10] = 2 * [1,2,3,4,5] if left elemination done then it's right elimination turn
        # 2. left(2k) = 2 * right(k)

        #relative ans of elemination game of left start w.r.t first elment i.e 1 == relative ans of elimination game of right start w.r.t last elemen i.e k
        # 3. left(k) - 1 = k - right(k)
        
        # 2k+1 will have the same answer as 2k
        if n % 2 == 1:
            n = n - 1
        # setting up the base case
        if not n:
            return 1
        # recursion step
        return n - 2 * (self.lastRemaining(n//2) - 1)

    def lastRemaining2(self, n: int) -> int:
        """
            Given a circular array of size n containing integers from 1 to n.
            Find the last element that would remain in the list after erasing
            every second element starting from the first element.
        :param n:
        :return:
        """
        if n == 1:
            return 1

        if n % 2 == 0:
            return 2 * self.lastRemaining(n / 2) - 1

        return 2 * self.lastRemaining((n - 1) / 2) + 1
