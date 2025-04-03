class Solution:
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:

    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.
    Example 2:

    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
    Example 3:

    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
    """
    def findMin1(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if (mid == 0 or nums[mid - 1] > nums[mid]) and (mid == n - 1 or nums[mid + 1] > nums[mid]):
                return mid
            elif mid == 0 or nums[mid - 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
    def findMin2(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # Check if mid element is smaller than both neighbors
            if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid == n - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            
            # Decide which half to search
            if nums[mid] > nums[r]:
                # Minimum is in the right half
                l = mid + 1
            else:
                # Minimum is in the left half (including mid)
                r = mid
        
        return nums[l]
    
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid == n - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]