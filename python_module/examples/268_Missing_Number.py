from typing import List


class Solution:
    """
        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

        Example 1:

        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
        Example 2:

        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
        Example 3:

        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


        Constraints:

        n == nums.length
        1 <= n <= 104
        0 <= nums[i] <= n
        All the numbers of nums are unique.
    """
    def missingNumber1(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        for i in range(len(nums)):
            while nums[i] >= 0 and nums[i] < len(nums) and nums[i] != i and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
    
    def missingNumber3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        for i in range(n):
            while nums[i] >= 0 and nums[i] < n and nums[i] != i and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        
        for i in range(n):
            if nums[i] != i:
                return i
        return n
    
    def findMissingNumber(nums):
        """
        Find the missing number in an array containing n distinct numbers in range [0, n]
        
        Args:
            nums: List[int] - Array of n distinct integers in range [0, n]
            
        Returns:
            int - The missing number
        """
        # Method 1: Using XOR
        # XOR all numbers from 0 to n and all numbers in array
        # The result will be the missing number
        n = len(nums)
        result = n  # Start with n since range is [0, n]
        
        # XOR with all indices and values
        for i in range(n):
            result ^= i ^ nums[i]
            
        return result
