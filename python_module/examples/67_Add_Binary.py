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

    def addBinary2(self, a: str, b: str) -> str:
        # List to store the result
        res = []
        carry = 0
        idxa, idxb = len(a) - 1, len(b) - 1
        while idxa >= 0 or idxb >= 0 or carry > 0:
            t = carry
            if idxa >= 0:
                t += int(a[idxa])
                idxa -= 1
            if idxb >= 0:
                t += int(b[idxb])
                idxb -= 1
            res.insert(0, str(t % 2))
            carry = t // 2
        return "".join(res)
    
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        arr_a = list(map(int, list(a)))
        arr_b = list(map(int, list(b)))

        res, idx1, idx2 = [], len(arr_a) - 1, len(arr_b) - 1
        carry = 0
        while idx1 >= 0 or idx2 >= 0 or carry > 0:
            value = carry
            if idx1 >= 0:
                value += arr_a[idx1]
                idx1 -= 1
            
            if idx2 >= 0:
                value += arr_b[idx2]
                idx2 -= 1
            carry = value // 2
            res.append(str(value % 2))
        
        return "".join(res[::-1])

