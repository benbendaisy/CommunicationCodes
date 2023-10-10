from typing import List


class Solution:
    """
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

    Example 1:

    Input: nums = [3,2,3]
    Output: [3]
    Example 2:

    Input: nums = [1]
    Output: [1]
    Example 3:

    Input: nums = [1,2]
    Output: [1,2]
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_counters = Counter(nums)
        n = len(nums)
        res = []
        for num, cnt in num_counters.items():
            if cnt > n // 3:
                res.append(num)
        return res