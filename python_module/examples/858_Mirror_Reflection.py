class Solution:
    """
        There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

        The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

        Given the two integers p and q, return the number of the receptor that the ray meets first.

        The test cases are guaranteed so that the ray will meet a receptor eventually.

        Example 1:

        Input: p = 2, q = 1
        Output: 2
        Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
        Example 2:

        Input: p = 3, q = 1
        Output: 1

        Constraints:

        1 <= q <= p <= 1000
    """
    def mirrorReflection1(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p, q = p // 2, q // 2
        return 1 - p % 2 + q % 2

    def mirrorReflection(self, p: int, q: int) -> int:
        """
            So, this problem can be transformed into finding m * p = n * q, where
            m = the number of room extension + 1.
            n = the number of light reflection + 1.
            If the number of light reflection is odd (which means n is even), it means the corner is on the left-hand side. The possible corner is 2.
            Otherwise, the corner is on the right-hand side. The possible corners are 0 and 1.
            Given the corner is on the right-hand side.
            If the number of room extension is even (which means m is odd), it means the corner is 1. Otherwise, the corner is 0.
            m is even & n is odd => return 0.
            m is odd & n is odd => return 1.
            m is odd & n is even => return 2.
            refer to https://leetcode.com/problems/mirror-reflection/discuss/2376191/C%2B%2B-Java-Python-or-Faster-then-100-or-Full-explanations-or
        :param p:
        :param q:
        :return:
        """
        while p % 2 == 0 and q % 2 == 0: # p & q are both even, divide both by 2
            p, q = p // 2, q // 2

        if p % 2 == 0:  # p is even
            return 2
        elif q % 2 == 0: # q is even
            return 0

        return 1 # p & q are odd

class Solution1:
    def lcm(self, x, y):
        return x * y // self.gcd(x, y)

    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return abs(x)


    def mirrorReflection(self, p: int, q: int) -> int:
        time_for_reflection = self.lcm(p, q)
        is_right_side = True if time_for_reflection/q % 2 == 1 else False
        is_top_side = True if time_for_reflection/p % 2 == 1 else False

        if is_right_side and is_top_side:
            return 1
        elif not is_right_side and is_top_side:
            return 2

        return 0