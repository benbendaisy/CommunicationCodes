from typing import List


class Solution:
    """
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:

    Input: nums = [1,1,1], k = 2
    Output: 2
    Example 2:

    Input: nums = [1,2,3], k = 3
    Output: 2
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        prefix_sum_cache = {0:1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_cache:
                res += prefix_sum_cache[prefix_sum - k]
            if prefix_sum not in prefix_sum_cache:
                prefix_sum_cache[prefix_sum] = 1
            else:
                prefix_sum_cache[prefix_sum] += 1
        return res
