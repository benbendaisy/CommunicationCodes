class Solution:
    """
    You are given a 0-indexed integer array nums.

    Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

    The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

    Example 1:

    Input: nums = [12,6,1,2,7]
    Output: 77
    Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
    It can be shown that there are no ordered triplets of indices with a value greater than 77. 
    Example 2:

    Input: nums = [1,10,3,4,19]
    Output: 133
    Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
    It can be shown that there are no ordered triplets of indices with a value greater than 133.
    Example 3:

    Input: nums = [1,2,3]
    Output: 0
    Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.
    """
    def maximumTripletValue1(self, nums: List[int]) -> int:
        """
        Time limit exceeded for large inputs.
        """
        if not nums or len(nums) < 3:
            return 0
        n = len(nums)
        max_arr = [0] * n
        max_arr[0] = nums[0]
        for i in range(1, n):
            max_arr[i] = max(max_arr[i - 1], nums[i])
        
        max_triplet = 0
        for j in range(1, n - 1):
            for k in range(j + 1, n):
                max_triplet = max(max_triplet, (max_arr[j - 1] - nums[j]) * nums[k])
        return max_triplet
    
    def maximumTripletValue2(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        n = len(nums)
        max_left = nums[0]  # Maximum before index j
        max_triplet = 0
        suffix_max = [0] * n
        suffix_max[n - 1] = nums[n - 1]
        
        # Compute suffix max in reverse
        for i in range(n - 2, 0, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        
        # Iterate for j in range(1, n-1)
        for j in range(1, n - 1):
            if max_left > nums[j] and suffix_max[j + 1] > 0:  # Ensure valid triplet
                max_triplet = max(max_triplet, (max_left - nums[j]) * suffix_max[j + 1])
            max_left = max(max_left, nums[j])  # Update max_left
        
        return max_triplet
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        n = len(nums)
        max_left = nums[0]

        max_right_arr = [0] * n
        max_right_arr[n - 1] = nums[-1]
        for i in range(n - 2, 0, -1):
            max_right_arr[i] = max(max_right_arr[i + 1], nums[i])
        
        max_triplet = 0
        for j in range(1, n - 1):
            max_triplet = max(max_triplet, (max_left - nums[j]) * max_right_arr[j + 1])
            max_left = max(max_left, nums[j])
        return max_triplet