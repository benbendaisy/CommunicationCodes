from typing import List


class Solution:
    """
    You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

    We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

    The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
    The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
    The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
    Return true if the array has at least one valid partition. Otherwise, return false.

    Example 1:

    Input: nums = [4,4,4,5,6]
    Output: true
    Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
    This partition is valid, so we return true.
    Example 2:

    Input: nums = [1,1,1,2]
    Output: false
    Explanation: There is no valid partition for this array.
    """
    def validPartition1(self, nums: List[int]) -> bool:
        def checking(left, right):
            if right - left == 1:
                return nums[left] == nums[right]
            elif nums[left] == nums[left + 1] and nums[left + 1] == nums[left + 2]:
                return True
            elif nums[left + 1] - nums[left] == 1 and nums[left + 2] - nums[left + 1] == 1:
                return True
            return False
        n = len(nums)
        @lru_cache(None)
        def helper(idx):
            if idx > n:
                return False
            if idx == n:
                return True
            two, three = False, False
            if idx < n - 1 and checking(idx, idx + 1):
                two = helper(idx + 2)
            if idx < n - 2 and checking(idx, idx + 2):
                three = helper(idx + 3)
            return two or three
        return helper(0)
    
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        # If the array has only one element, then not possible 
        # to partition into valid subarrays
        if n == 1:
            return False
        
        # Initialization for the first three values
        dp = [True, False, nums[0] == nums[1] if n > 1 else False]

        for i in range(2, n):
            current_dp = False
            # Check for 2 equal elements
            if nums[i] == nums[i - 1] and dp[1]:
                current_dp = True
            # Check for 3 equal elements
            elif nums[i] == nums[i - 1] == nums[i - 2] and dp[0]:
                current_dp = True
            # Check for 3 consecutive increasing elements 
            elif nums[i] - nums[i - 1] == 1 and nums[i - 1] - nums[i - 2] == 1 and dp[0]: 
                current_dp = True 
            # Move the window forward
            dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp
        return dp[2]
