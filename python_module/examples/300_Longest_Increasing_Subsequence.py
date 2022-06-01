from bisect import bisect_left
from typing import List


class Solution:
    """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
        For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

        Example 1:

        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        Example 2:

        Input: nums = [0,1,0,3,2,3]
        Output: 4
        Example 3:

        Input: nums = [7,7,7,7,7,7,7]
        Output: 1

        Constraints:

        1 <= nums.length <= 2500
        -104 <= nums[i] <= 104
    """
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)
        dp = [1] * length

        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])

        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sub = []
        for num in nums:
            idx = bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)
