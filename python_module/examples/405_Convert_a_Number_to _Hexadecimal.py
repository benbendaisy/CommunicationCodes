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

    def toHex2(self, num: int) -> str:
        if num == 0:
            return "0"
        mappings = "0123456789abcdef"
        res = ""
        for i in range(8):
            res = mappings[num & 15] + res
            num >>= 4
        return res.lstrip("0")
    
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = []
        
        # Convert negative numbers to 32-bit unsigned representation
        num &= 0xFFFFFFFF  # Handles two’s complement
        
        while num:
            result.append(hex_chars[num & 0xF])  # Extract last 4 bits
            num >>= 4  # Shift right by 4 bits
        
        return "".join(result[::-1])  # Reverse and join

