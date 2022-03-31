from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        for i in range(len(nums)):
            while nums[i] >= 0 and nums[i] < len(nums) and nums[i] != i and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

if __name__ == "__main__":
    nums = [3,0,1]
    solution = Solution()
    ret = solution.missingNumber(nums)
    print(ret)