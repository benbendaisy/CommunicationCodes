from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = list(map(lambda x:a * x**2 + b*x + c, nums))
        nums.sort()
        return nums