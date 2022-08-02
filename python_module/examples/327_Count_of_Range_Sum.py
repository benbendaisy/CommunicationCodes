from typing import List

class Solution:
    """
        Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

        Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

        Example 1:

        Input: nums = [-2,5,-1], lower = -2, upper = 2
        Output: 3
        Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
        Example 2:

        Input: nums = [0], lower = 0, upper = 0
        Output: 1

        Constraints:

        1 <= nums.length <= 105
        -231 <= nums[i] <= 231 - 1
        -105 <= lower <= upper <= 105
        The answer is guaranteed to fit in a 32-bit integer.
    """
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        x = SortedList([])
        p = [0]
        for num in nums:
            p.append(p[-1] + num)
        for i in range(len(nums) - 1, -1, -1):
            x.add(p[i + 1])
            ans += x.bisect_right(p[i] + upper) - x.bisect_left(p[i] + lower)
        return ans