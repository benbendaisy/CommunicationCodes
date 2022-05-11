from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
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