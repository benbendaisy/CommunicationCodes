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

    def singleNumber(self, nums: List[int]) -> List[int]:
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

if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    solution = Solution()
    ret = solution.singleNumber(nums)
    print(ret)