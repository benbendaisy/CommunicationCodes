from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        cur = len(nums) - 2
        while cur >= 0 and nums[cur + 1] <= nums[cur]:
            cur -= 1

        if cur >= 0: # swap the num just less than current num
            r = len(nums) - 1
            while r > cur and nums[r] <= nums[cur]:
                r -= 1
            nums[cur], nums[r] = nums[r], nums[cur]

        l, r = cur + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

if __name__ == "__main__":
    nums = [5, 1, 1]
    solution = Solution()
    ret = solution.nextPermutation(nums)
    print(nums)

