from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return -1

        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[i] > 0 and nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        return 0

if __name__ == "__main__":
    nums = [1,3,4,2,2]
    solution = Solution()
    ret = solution.findDuplicate(nums)
    print(ret)