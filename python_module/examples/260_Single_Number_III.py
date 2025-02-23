from typing import List
from collections import Counter

class Solution:
    def singleNumber1(self, nums: List[int]) -> List[int]:
        hashMap = Counter(nums)

        res = []
        for key, val in hashMap.items():
            if val == 1:
                res.append(key)

        return res

    def singleNumber2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    cnt += 1
            cnt %= 2
            res |= cnt << i
        
        for num in nums:
            xorValue = res ^ num
            xorValue = xorValue if xorValue < (1 << 31) else xorValue - (1 << 32)
            try:
                if nums.index(xorValue) != -1:
                    return [num, xorValue]
            except ValueError:
                ""
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        step1: xor all numbers to get xor of the two unique numbers
        step2: trying to find the rightmost bit that is 1 from the xor result
        step3: divide elements into two groups based on the rightmost set bit
        and xor elements in each group
        """
        # Step 1: XOR all numbers to get XOR of the two unique numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Step 2: Find rightmost set bit in xor_result
        # This bit will be set in one unique number and unset in the other
        rightmost_set_bit = xor_result & -xor_result
        
        # Step 3: Divide elements into two groups based on the rightmost set bit
        # and XOR elements in each group
        x = y = 0
        for num in nums:
            if num & rightmost_set_bit:  # Bit is set
                x ^= num
            else:  # Bit is not set
                y ^= num
        
        return [x, y]

if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    solution = Solution()
    ret = solution.singleNumber(nums)
    print(ret)