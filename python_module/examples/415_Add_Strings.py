class Solution:
    """
        Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

        You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

        Example 1:

        Input: num1 = "11", num2 = "123"
        Output: "134"
        Example 2:

        Input: num1 = "456", num2 = "77"
        Output: "533"
        Example 3:

        Input: num1 = "0", num2 = "0"
        Output: "0"
    """
    def addStrings1(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        l1, l2 = m - 1, n - 1
        res = ""
        carrier = 0
        while l1 >= 0 and l2 >= 0:
            t = int(num1[l1]) + int(num2[l2]) + carrier
            res = str(t % 10) + res
            carrier = t // 10
            l1 -= 1
            l2 -= 1
        while l1 >= 0:
            t = int(num1[l1]) + carrier
            res = str(t % 10) + res
            carrier = t // 10
            l1 -= 1

        while l2 >= 0:
            t = int(num2[l2]) + carrier
            res = str(t % 10) + res
            carrier = t // 10
            l2 -= 1

        if carrier > 0:
            res = str(carrier) + res

        return res

    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        p1, p2 = m - 1, n - 1
        res = []
        carrier = 0
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            t = x1 + x2 + carrier
            res.append(t % 10)
            carrier = t // 10
            p1 -= 1
            p2 -= 1
        if carrier > 0:
            res.append(carrier)
        return "".join(str(x) for x in res[::-1])
