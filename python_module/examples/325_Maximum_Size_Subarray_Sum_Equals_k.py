from typing import List


class Solution:
    """
        Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.

        Example 1:

        Input: nums = [1,-1,5,-2,3], k = 3
        Output: 4
        Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
        Example 2:

        Input: nums = [-2,-1,2,1], k = 1
        Output: 2
        Explanation: The subarray [-1, 2] sums to 1 and is the longest.

        Constraints:

        1 <= nums.length <= 2 * 105
        -104 <= nums[i] <= 104
        -109 <= k <= 109
    """
    def maxSubArrayLen1(self, nums: List[int], k: int) -> int:
         if not nums:
             return 0
         elif len(nums) == 1:
             return 1 if nums[0] == k else 0
         n = len(nums)
         res = []
         for i in range(n):
             for j in range(i + 1, n + 1):
                 subArray = nums[i:j]
                 if sum(subArray) == k and len(subArray) > len(res):
                     res = subArray
         return len(res)

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        preSum = longestSub = 0
        indexes = {}
        for i, num in enumerate(nums):
            preSum += num
            if preSum == k:
                longestSub = i + 1

            if preSum - k in indexes:
                longestSub = max(longestSub, i - indexes[preSum - k])

            if preSum not in indexes:
                indexes[preSum] = i
        return longestSub
