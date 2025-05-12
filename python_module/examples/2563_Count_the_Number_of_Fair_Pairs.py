class Solution:
    """
    Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

    A pair (i, j) is fair if:

    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper
    

    Example 1:

    Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
    Output: 6
    Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
    Example 2:

    Input: nums = [1,7,9,2,5], lower = 11, upper = 11
    Output: 1
    Explanation: There is a single fair pair: (2,3).
    """
    def countFairPairs1(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time Limit Exceeded
        """
        if not nums:
            return 0
        
        cnt, n = 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if lower <= nums[i] + nums[j] <= upper:
                    cnt += 1
        return cnt
    
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0

        for i in range(n):
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            left = bisect_left(nums, min_val, i + 1)
            right = bisect_right(nums, max_val, i + 1)
            cnt += right - left

        return cnt