from functools import lru_cache
from typing import List


class Solution:
    """
    You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

    In the ith operation (1-indexed), you will:

    Choose two elements, x and y.
    Receive a score of i * gcd(x, y).
    Remove x and y from nums.
    Return the maximum score you can receive after performing n operations.

    The function gcd(x, y) is the greatest common divisor of x and y.

    Example 1:

    Input: nums = [1,2]
    Output: 1
    Explanation: The optimal choice of operations is:
    (1 * gcd(1, 2)) = 1
    Example 2:

    Input: nums = [3,4,6,8]
    Output: 11
    Explanation: The optimal choice of operations is:
    (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
    Example 3:

    Input: nums = [1,2,3,4,5,6]
    Output: 14
    Explanation: The optimal choice of operations is:
    (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
    """
    def maxScore1(self, nums: List[int]) -> int:
        @lru_cache(None)
        def fn(array, n):
            if not array:
                return 0
            
            ans = 0
            for i in range(len(array)):
                for j in range(i + 1, len(array)):
                    rest = array[:i] + array[i + 1 : j] + array[j + 1:]
                    ans = max(ans, n * gcd(array[i], array[j]) + fn(tuple(rest), n + 1))
            return ans
        
        return fn(tuple(nums), 1)
    
    def maxScore(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = (len(nums) // 2)
        @cache
        def helper(idx: int, mask: int):
            if idx == n + 1:
                return 0
            max_sum = float('-inf')
            for i in range(2 * n):
                for j in range(i + 1, 2 * n):
                    if ((1 << i) & mask) == 0 and ((1 << j) & mask) == 0:
                        new_mask = mask | (1 << i)
                        new_mask = new_mask | (1 << j)
                        local_sum = idx * gcd(nums[i], nums[j]) + helper(idx + 1, new_mask)
                        max_sum = max(max_sum, local_sum)
            return max_sum
        return helper(1, 0)