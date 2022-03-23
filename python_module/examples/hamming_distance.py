class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        cnt = 0
        while xor:
            xor = xor & (xor - 1)
            cnt += 1
        return cnt

    def hammingDistance1(self, x: int, y: int) -> int:
        xor = x ^ y
        cnt = 0
        while xor:
            cnt += xor & 1
            xor >>= 1
        return cnt