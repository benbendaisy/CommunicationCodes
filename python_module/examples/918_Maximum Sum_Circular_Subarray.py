import math
from typing import List


class Solution:
    """
        Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

        A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

        A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

        Example 1:

        Input: nums = [1,-2,3,-2]
        Output: 3
        Explanation: Subarray [3] has maximum sum 3.
        Example 2:

        Input: nums = [5,-3,5]
        Output: 10
        Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
        Example 3:

        Input: nums = [-3,-2,-3]
        Output: -2
        Explanation: Subarray [-2] has maximum sum -2.
    """
    def maxSubarraySumCircular1(self, nums: List[int]) -> int:
        total_sum = 0
        cur_max_sum = 0
        cur_min_sum = 0
        max_sum = -math.inf
        min_sum = math.inf
        for num in nums:
            total_sum += num
            cur_max_sum = max(cur_max_sum + num, num)
            cur_min_sum = min(cur_min_sum + num, num)
            max_sum = max(max_sum, cur_max_sum)
            min_sum = min(min_sum, cur_min_sum)
        return max_sum if max_sum < 0 else max(max_sum, total_sum - min_sum)
    
    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = len(nums)
        def helper(arr: List[int]):
            max_sum, running_sum = float('-inf'), 0
            for num in arr:
                if running_sum < 0:
                    running_sum = num
                else:
                    running_sum += num
                max_sum = max(max_sum, running_sum)
            return max_sum
        
        total_sum = sum(nums)
        max_sum = helper(nums)
        if max_sum < 0:
            return max_sum
        invert_nums = [-num for num in nums]
        min_sum = -helper(invert_nums)
        max_circular = total_sum - min_sum
        return max(max_sum, max_circular)
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = len(nums)
        running_max_sum, running_min_sum = 0, 0
        max_sum, min_sum = float('-inf'), float('inf')
        total_sum = sum(nums)
        for num in nums:
            running_max_sum = max(running_max_sum + num, num)
            running_min_sum = min(running_min_sum + num, num)
            max_sum = max(max_sum, running_max_sum)
            min_sum = min(min_sum, running_min_sum)
        return max_sum if max_sum < 0 else max(max_sum, total_sum - min_sum)