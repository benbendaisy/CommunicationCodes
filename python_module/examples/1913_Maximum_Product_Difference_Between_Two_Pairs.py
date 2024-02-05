from typing import List


class Solution:
    """
    The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

    For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
    Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

    Return the maximum such product difference.

    Example 1:

    Input: nums = [5,6,2,7,4]
    Output: 34
    Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
    The product difference is (6 * 7) - (2 * 4) = 34.
    Example 2:

    Input: nums = [4,2,5,9,7,4,8]
    Output: 64
    Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
    The product difference is (9 * 8) - (2 * 4) = 64.
    """
    def maxProductDifference1(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        smallest = inf
        second_smallest = inf

        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
            
            if num < smallest:
                second_smallest = smallest
                smallest = num
            else:
                second_smallest = min(second_smallest, num)
        return biggest * second_biggest - smallest * second_smallest 
    
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]