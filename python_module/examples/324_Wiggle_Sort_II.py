from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return

        n = len(nums)
        l = sorted(nums)
        for i in range(1, n, 2):
            nums[i] = l.pop()

        for i in range(0, n, 2):
            nums[i] = l.pop()
