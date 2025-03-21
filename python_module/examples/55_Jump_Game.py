from typing import List


class Solution:
    """
        You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.

        Example 1:

        Input: nums = [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
        Example 2:

        Input: nums = [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    """
    def canJump1(self, nums: List[int]) -> bool:
        max_step = 0
        for idx, val in enumerate(nums):
            if idx > max_step:
                return False
            max_step = max(max_step, idx + val)
        return True
    
    def canJump2(self, nums: List[int]) -> bool:
        if not nums:
            return False
        max_step = 0
        for idx, num in enumerate(nums):
            if max_step < idx:
                return False
            max_step = max(max_step, idx + num)
        return True
    
    def canJump3(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n, jump = len(nums), nums[0]
        for i in range(1, n):
            if jump == 0:
                return False
            jump = max(jump - 1, nums[i])
        return True
    
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        max_step = 0
        for i, v in enumerate(nums):
            if max_step < i:
                return False
            max_step = max(max_step, i + v)
        return True