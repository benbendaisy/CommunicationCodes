from functools import lru_cache
from typing import List


class Solution:
    """
        Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

        answer[i] % answer[j] == 0, or
        answer[j] % answer[i] == 0
        If there are multiple solutions, return any of them.

        Example 1:

        Input: nums = [1,2,3]
        Output: [1,2]
        Explanation: [1,3] is also accepted.
        Example 2:

        Input: nums = [1,2,4,8]
        Output: [1,2,4,8]

        Constraints:

        1 <= nums.length <= 1000
        1 <= nums[i] <= 2 * 109
        All the integers in nums are unique.
    """
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @lru_cache(None)
        def ends(idx):
            maxSet = []
            for p in range(idx):
                if nums[idx] % nums[p] == 0:
                    sub = ends(p)
                    if len(sub) > len(maxSet):
                        maxSet = sub

            return maxSet + [nums[idx]]

        if len(nums) == 0:
            return []
        nums.sort()
        return max([ends(i) for i in range(len(nums))], key=len)
