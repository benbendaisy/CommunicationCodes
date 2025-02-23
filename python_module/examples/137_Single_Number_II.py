from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        if not nums:
            return -1

        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                if ((num >> i) & 1) == 1:
                    cnt += 1
            cnt %= 3
            res |= cnt << i

        return res if res < (1 << 31) else res - (1 << 32)
    
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # Check each of the 32 bits
        for i in range(32):
            # Count number of elements with 1 at position i
            bit_sum = 0
            for num in nums:
                # Right shift num by i and check if least significant bit is 1
                bit_sum += (num >> i) & 1
            
            # If bit_sum mod 3 is 1, then the single number has 1 at position i
            if bit_sum % 3 == 1:
                # Handle two's complement for negative numbers
                if i == 31:
                    res -= (1 << 31)
                else:
                    res |= (1 << i)
        return res