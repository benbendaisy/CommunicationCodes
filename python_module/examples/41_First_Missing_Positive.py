from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        for i in range(len(nums)):
            while 0 <= nums[i] < len(nums) and nums[i] != i and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i

        return len(nums) + 1 if nums[0] == len(nums) else len(nums)