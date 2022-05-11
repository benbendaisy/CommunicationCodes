from typing import List


class Solution:
    def threeSumSmaller1(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        cnt = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] < target:
                        cnt += 1
        return cnt

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        nums.sort()

        def twoSumSmaller(idx: int, t: int):
            l, r = idx, len(nums) - 1
            cnt = 0
            while l < r:
                if nums[l] + nums[r] < t:
                    cnt += r - l
                    l += 1
                else:
                    r -= 1
            return cnt

        cnt = 0
        for i in range(len(nums) - 2):
            cnt += twoSumSmaller(i + 1, target - nums[i])
        return cnt