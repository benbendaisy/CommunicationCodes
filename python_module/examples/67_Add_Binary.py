class Solution:
    """
        Given two binary strings a and b, return their sum as a binary string.

        Example 1:

        Input: a = "11", b = "1"
        Output: "100"
        Example 2:

        Input: a = "1010", b = "1011"
        Output: "10101"
    """
    def addBinary1(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        idxa, idxb = la - 1, lb - 1
        res = []
        carrier = 0
        while idxa >= 0 and idxb >= 0:
            ch = (int(a[idxa]) + int(b[idxb]) + carrier) % 2
            res.insert(0, ch)
            carrier = (int(a[idxa]) + int(b[idxb]) + carrier) // 2
            idxa -= 1
            idxb -= 1

        while idxa >= 0:
            res.insert(0, (int(a[idxa]) + carrier) % 2)
            carrier = (int(a[idxa]) + carrier) // 2
            idxa -= 1

        while idxb >= 0:
            res.insert(0, (int(b[idxb]) + carrier) % 2)
            carrier = (int(b[idxb]) + carrier) // 2
            idxb -= 1

        if carrier > 0:
            res.insert(0, carrier)

        return "".join([str(ch) for ch in res])

    def addBinary(self, a: str, b: str) -> str:
        # List to store the result
        res = []
        carry = 0
        idxa, idxb = len(a) - 1, len(b) - 1
        while idxa >= 0 or idxb >= 0 or carry:
            total = carry
            if idxa >= 0:
                total += int(a[idxa])
                idxa -= 1
            if idxb >= 0:
                total += int(b[idxb])
                idxb -= 1
            res.insert(0, total % 2)
            carry = total // 2
        return "".join([str(ch) for ch in res])

