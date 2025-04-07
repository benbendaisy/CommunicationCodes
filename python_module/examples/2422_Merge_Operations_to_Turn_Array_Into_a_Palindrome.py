class Solution:
    """
    You are given an array nums consisting of positive integers.

    You can perform the following operation on the array any number of times:

    Choose any two adjacent elements and replace them with their sum.
    For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
    Return the minimum number of operations needed to turn the array into a palindrome.

    Example 1:

    Input: nums = [4,3,2,1,2,3,1]
    Output: 2
    Explanation: We can turn the array into a palindrome in 2 operations as follows:
    - Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
    - Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
    The array [4,3,2,3,4] is a palindrome.
    It can be shown that 2 is the minimum number of operations needed.
    Example 2:

    Input: nums = [1,2,3,4]
    Output: 3
    Explanation: We do the operation 3 times in any position, we obtain the array [10] at the end which is a palindrome.
    """
    def minimumOperations1(self, nums: List[int]) -> int:
        def helper(arr: List[int]):
            if not arr or len(arr) == 1 or arr == arr[::-1]:
                return 0
            
            min_ops = float('inf')
            for i in range(1, len(arr)):
                min_ops = min(min_ops, 1 + helper(arr[:i - 1] + [arr[i] + arr[i - 1]] + arr[i + 1:]))
            return min_ops
        
        return helper(nums)
    
    def minimumOperations2(nums: List[int]) -> int:
        @cache
        def helper(arr: tuple) -> int:
            if not arr or len(arr) == 1 or arr == arr[::-1]:
                return 0
            
            min_ops = float('inf')
            for i in range(1, len(arr)):
                new_arr = arr[:i - 1] + (arr[i] + arr[i - 1],) + arr[i + 1:]
                min_ops = min(min_ops, 1 + helper(new_arr))
            return min_ops
        
        return helper(tuple(nums))
    
    def minimumOperations3(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        operations = 0
        
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                left += 1
                operations += 1
            else:
                nums[right - 1] += nums[right]
                right -= 1
                operations += 1
        
        return operations
    
    def minimumOperations4(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        left, right = 0, len(nums) - 1
        ops = 0
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                left += 1
                ops += 1
            else:
                nums[right - 1] += nums[right]
                right -= 1
                ops += 1
        return ops