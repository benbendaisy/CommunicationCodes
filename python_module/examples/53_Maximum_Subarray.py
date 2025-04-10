class Solution:
    """
    Given an integer array nums, find the subarray
    with the largest sum, and return its sum.

    Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    Example 2:

    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.
    Example 3:

    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
    """
    def maxSubArray1(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        running_sum, max_sum = 0, float('-inf')
        for num in nums:
            if running_sum < 0:
                running_sum = num
            else:
                running_sum += num
            max_sum = max(max_sum, running_sum)
                
        return max_sum
    
    def maxSubArray2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum, running_sum = float('-inf'), 0
        for num in nums:
            if running_sum < 0:
                running_sum = num
            else:
                running_sum += num
            max_sum = max(running_sum, max_sum)
        return max_sum
    
    def maxSubArray3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum, running_sum = float('-inf'), 0
        for num in nums:
            if running_sum < 0:
                running_sum = num
            else:
                running_sum += num
            max_sum = max(max_sum, running_sum)
        return max_sum
    
    def maxSubArray4(self, nums: List[int]) -> int:
        if not nums:
            return 0
        running_sum, max_sum = 0, float('-inf')
        for num in nums:
            if running_sum < 0:
                running_sum = num
            else:
                running_sum += num
            max_sum = max(max_sum, running_sum)
            
        return max_sum
    
    def maxSubArray5(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sub = float('-inf')
        running_sum, n = float('-inf'), len(nums)
        for i in range(n):
            if running_sum < 0:
                running_sum = nums[i]
            else:
                running_sum += nums[i]
            max_sub = max(max_sub, running_sum)
        
        return max_sub
    
    def maxSubArray6(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        running_sum = max_sum = nums[0]  # Initialize with the first element
        for num in nums[1:]:
            running_sum = max(num, running_sum + num)
            max_sum = max(max_sum, running_sum)
        
        return max_sum  # Return max_sum instead of running_sum
    
    def maxSubArray7(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        running_sum, max_sum = 0, nums[0]
        for num in nums:
            running_sum = max(num, running_sum + num)
            max_sum = max(max_sum, running_sum)
        return max_sum
