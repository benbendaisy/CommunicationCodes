import math
from typing import List


class Solution:
    """
        You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

        Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

        Example 1:

        Input: nums = [1,1,4,2,3], x = 5
        Output: 2
        Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
        Example 2:

        Input: nums = [5,6,7,8,9], x = 4
        Output: -1
        Example 3:

        Input: nums = [3,2,20,1,1,3], x = 10
        Output: 5
        Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

        Constraints:

        1 <= nums.length <= 105
        1 <= nums[i] <= 104
        1 <= x <= 109
    """
    def minOperations1(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        current = 0
        left = 0
        max_length = -math.inf
        for right in range(n):
            current += nums[right]
            while current > total - x and left <= right:
                current -= nums[left]
                left += 1
            if current == total - x:
                max_length = max(max_length, right - left + 1)
        return n - max_length if max_length != -math.inf else -1

    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        current = sum(nums)
        left = 0
        min_length = math.inf
        for right in range(n):
            current -= nums[right]
            while current < x and left <= right:
                current += nums[left]
                left += 1
            if current == x:
                min_length = min(min_length, n - (right - left + 1))
        return min_length if min_length != math.inf else -1


