class Solution:
    def toHex1(self, num: int) -> str:
        if num == 0:
            return "0"

        mappings = "0123456789abcdef"
        res = ""
        for i in range(8):
            res = mappings[num % 16] + res
            num //= 16
        return res.lstrip("0")

    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        mappings = "0123456789abcdef"
        res = ""
        for i in range(8):
            res = mappings[num & 15] + res
            num >>= 4
        return res.lstrip("0")

