from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        for i in range(len(nums)):
            while nums[i] != i and nums[i] < len(nums) and nums[i] > 0 and nums[nums[i]] != nums[i]:
                # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i

        return len(nums) + 1 if nums[0] == len(nums) else len(nums)

if __name__ == "__main__":
    nums = [1,2,0]
    solution = Solution()
    ret = solution.firstMissingPositive(nums)
    print(ret)