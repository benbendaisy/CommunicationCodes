from typing import List


class Solution:
    """
        Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

        You must write an algorithm that runs in O(n) time and uses only constant extra space.

        Example 1:

        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [2,3]
        Example 2:

        Input: nums = [1,1,2]
        Output: [1]
        Example 3:

        Input: nums = [1]
        Output: []
    """
    def findDuplicates1(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            n = abs(num)
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] = -nums[n - 1]
        return res

    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idx = 0
        while idx < n:
            cur_idx = nums[idx] - 1
            if nums[idx] != nums[cur_idx]:
                nums[idx], nums[cur_idx] = nums[cur_idx], nums[idx]
            else:
                idx += 1
        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res