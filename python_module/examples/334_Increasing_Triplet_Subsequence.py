import math
from bisect import bisect_left
from typing import List


class Solution:
    """
        Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

        Example 1:

        Input: nums = [1,2,3,4,5]
        Output: true
        Explanation: Any triplet where i < j < k is valid.
        Example 2:

        Input: nums = [5,4,3,2,1]
        Output: false
        Explanation: No triplet exists.
        Example 3:

        Input: nums = [2,1,5,0,4,6]
        Output: true
        Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

        Constraints:

        1 <= nums.length <= 5 * 105
        -231 <= nums[i] <= 231 - 1

        Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
    """
    def increasingTriplet1(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        if not nums:
            return False

        first = math.inf
        second = math.inf
        for num in nums:
            if num < first:
                first = num
            elif num < second:
                second = num
            else:
                return True
        return False

    def increasingTriplet4(self, nums: List[int]) -> bool:
        if not nums:
            return False

        sub = []
        k = 3
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
                if len(sub) == 3:
                    return True
            else:
                for i in range(len(sub), 0, -1):
                    if sub[i] >= num:
                        sub[i] = num
                        break
        return False

    def increasingTriplet5(self, nums: List[int]) -> bool:
        if not nums:
            return False

        sub = []
        k = 3
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
                if len(sub) == 3:
                    return True
            else:
                idx = bisect_left(sub, num)
                sub[idx] = num
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        firstNum, lastNum = math.inf, math.inf
        for num in nums:
            if num <= firstNum:
                firstNum = num
            elif num <= lastNum:
                lastNum = num
            else:
                return True
        return False
