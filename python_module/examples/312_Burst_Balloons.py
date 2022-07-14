from typing import List


class Solution:
    """
        You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

        If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

        Return the maximum coins you can collect by bursting the balloons wisely.

        Example 1:

        Input: nums = [3,1,5,8]
        Output: 167
        Explanation:
        nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
        coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
        Example 2:

        Input: nums = [1,5]
        Output: 10

        Constraints:

        n == nums.length
        1 <= n <= 300
        0 <= nums[i] <= 100
    """
    def __init__(self):
        self.memoDict = dict()
    def maxCoins(self, nums: List[int]) -> int:
        if tuple(nums) in self.memoDict:
            return self.memoDict[tuple(nums)]
        if len(nums) == 1:
            return nums[0]
        maxCoin = 0
        for i in range(len(nums)):
            a = 1 if i == 0 else nums[i - 1]
            b = 1 if i == len(nums) - 1 else nums[i + 1]
            t = a * b * nums[i]
            maxCoin = max(maxCoin, t + self.maxCoins(nums[:i] + nums[i + 1:]))
        self.memoDict[tuple(nums)] = maxCoin
        return maxCoin

