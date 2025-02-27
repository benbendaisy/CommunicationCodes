class Solution:
    """
    You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

    For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
    Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

    An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

    Example 1:

    Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
    Output: 1
    Explanation: 
    Swap nums1[3] and nums2[3]. Then the sequences are:
    nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
    which are both strictly increasing.
    Example 2:

    Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
    Output: 1
    """
    def minSwap1(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2 or len(nums1) != len(nums2):
            return -1
        m = len(nums1)
        def valid(nums: List[int]):
            n = len(nums)
            for i in range(n - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        def swap(idx: int):
            t = nums1[idx]
            nums1[idx] = nums2[idx]
            nums2[idx] = t

        def helper(idx: int):
            if idx == m:
                if valid(nums1) and valid(nums2):
                    return 0
                return float('inf')
            
            swap(idx)
            do_swap = 1 + helper(idx + 1)
            swap(idx)

            not_swap = helper(idx + 1)
            
            return min(do_swap, not_swap)
        
        return helper(0)
    
    def minSwap2(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @cache
        def backtrack(index, prev1, prev2):
            # Base case: reached the end of arrays
            if index == n:
                return 0
            
            # Initialize result to a large value
            result = float('inf')
            
            # Current values in each array
            curr1, curr2 = nums1[index], nums2[index]
            
            # Option 1: Don't swap at this position
            if curr1 > prev1 and curr2 > prev2:
                result = min(result, backtrack(index + 1, curr1, curr2))
            
            # Option 2: Swap at this position
            if curr2 > prev1 and curr1 > prev2:
                result = min(result, 1 + backtrack(index + 1, curr2, curr1))
        
            return result

        return backtrack(0, float('-inf'), float('-inf'))  # Start at index 0 with no swap
    
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @cache
        def helper(idx: int, prev1: int, prev2: int):
            if idx == n:
                return 0
            
            cur1, cur2 = nums1[idx], nums2[idx]
            res = float('inf')
            if prev1 < cur1 and prev2 < cur2:
                res = min(res, helper(idx + 1, cur1, cur2))
            
            if prev1 < cur2 and prev2 < cur1:
                res = min(res, 1 + helper(idx + 1, cur2, cur1))
            
            return res
        return helper(0, float('-inf'), float('-inf'))