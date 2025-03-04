from typing import List


class Solution:
    """
        Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

        The test cases are generated so that the answer can fit in a 32-bit integer.

        Example 1:

        Input: nums = [1,2,3], target = 4
        Output: 7
        Explanation:
        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
        Note that different sequences are counted as different combinations.
        Example 2:

        Input: nums = [9], target = 3
        Output: 0

        Constraints:

        1 <= nums.length <= 200
        1 <= nums[i] <= 1000
        All the elements of nums are unique.
        1 <= target <= 1000

    """
    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        nums.sort()
        def combinationSum(remain):
            if remain == 0:
                return 1

            res = 0
            for num in nums:
                if remain >= num:
                    res += combinationSum(remain - num)

        return combinationSum(target)

    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(target + 1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t - num]

        return dp[target]
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        @cache
        def helper(running_sum: int) -> int:
            if running_sum == target:
                return 1

            num_ways = 0
            for num in nums:
                new_running_sum = num + running_sum
                if new_running_sum <= target:
                    num_ways += helper(new_running_sum)
            return num_ways
        
        return helper(0)
