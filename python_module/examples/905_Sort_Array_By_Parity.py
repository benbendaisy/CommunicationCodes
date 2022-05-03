from typing import List


class Solution:
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        current = runner = 0
        while current < len(nums) and nums[current] % 2 == 0:
            current += 1

        runner = current + 1
        while runner < len(nums):
            while runner < len(nums) and nums[runner] % 2 != 0:
                runner += 1
            if runner < len(nums):
                nums[current], nums[runner] = nums[runner], nums[current]
            current, runner = current + 1, runner + 1

        return nums

    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: x % 2)
        return nums

    def sortArrayByParity3(self, nums: List[int]) -> List[int]:
        nums1 = [x for x in nums if x % 2 == 0]
        nums2 = [x for x in nums if x % 2 != 0]
        return nums1 + nums2

    def sortArrayByParity4(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            while l < r and nums[l] %  2 == 0:
                l += 1

            while r > l and nums[r] % 2 != 0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]

            l, r = l + 1, r - 1

        return nums

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]

            if nums[l] % 2 == 0: l += 1
            if nums[r] % 2 != 0: r -= 1

        return nums
