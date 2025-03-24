class Solution:
    """
    Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:

    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    Example 2:

    Input: target = 4, nums = [1,4,4]
    Output: 1
    Example 3:

    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return -1
        
        running_sum, left = 0, 0
        min_length = float('inf')
        for i, v in enumerate(nums):
            running_sum += v
            while running_sum >= target:
                min_length = min(min_length, i - left + 1)
                running_sum -= nums[left]
                left += 1
            
        return min_length if min_length != float('inf') else 0
