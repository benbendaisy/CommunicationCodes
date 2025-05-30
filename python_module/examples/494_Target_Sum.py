class Solution:
    """
    You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.

    Example 1:

    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3
    Example 2:

    Input: nums = [1], target = 1
    Output: 1
    """
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        m = len(nums)

        @cache
        def helper(idx: int, path_sum: int):
            if idx == m:
                if path_sum == target:
                    return 1
                return 0
            
            return helper(idx + 1, path_sum + nums[idx]) + helper(idx + 1, path_sum - nums[idx])
        return helper(0, 0)
    
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        @cache
        def helper(idx: int, t: int) -> int:
            if idx == n:
                return t == target
            
            return helper(idx + 1, t + nums[idx]) + helper(idx + 1, t - nums[idx])
        
        return helper(0, 0)
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        @cache
        def helper(idx: int, sums: int):
            if idx == n:
                return sums == target
            
            return helper(idx + 1, sums + nums[idx]) + helper(idx + 1, sums - nums[idx])
        
        return helper(0, 0)