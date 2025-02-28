class Solution:
    """
    Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

    Return the minimized largest sum of the split.

    A subarray is a contiguous part of the array.

    Example 1:

    Input: nums = [7,2,5,10,8], k = 2
    Output: 18
    Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
    Example 2:

    Input: nums = [1,2,3,4,5], k = 2
    Output: 9
    Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
    """
    def splitArray1(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        def get_max_sum(patitions: List[List[int]]):
            max_sum = 0
            for lst in patitions:
                max_sum = max(max_sum, sum(lst))
            return max_sum
        n = len(nums)
        min_max_sum = float('inf')
        def helper(path: List[List[int]], idx: int, p: int):
            nonlocal min_max_sum
            if idx == n:
                return

            if p == 1:
                path.append(nums[idx:])
                min_max_sum = min(min_max_sum, get_max_sum(path))
                return
            
            for i in range(idx, n):
                helper(path + [nums[idx: i + 1]], i + 1, p - 1)
            
        helper([], 0, k)
        return min_max_sum
    
    def splitArray2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @lru_cache(None)  # Memoization to avoid recomputation
        def dp(idx: int, k: int) -> int:
            if k == 1:  # Base case: Only one partition left
                return sum(nums[idx:])  # The rest of the array is the partition
            
            min_max_sum = float('inf')
            cur_sum = 0
            
            for i in range(idx, n - k + 1):  # Ensure at least k parts remain
                cur_sum += nums[i]  # Sum up the first partition
                max_partition_sum = max(cur_sum, dp(i + 1, k - 1))  # Recursive call
                
                min_max_sum = min(min_max_sum, max_partition_sum)  # Minimize the largest sum
                
                if cur_sum > min_max_sum:
                    break  # Prune search space (early stopping)
            
            return min_max_sum
        
        return dp(0, k)
    
    def splitArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        @cache
        def helper(idx: int, p: int):
            if p == 1:
                return sum(nums[idx:])
            
            min_max_sum = float('inf')
            cur_sum = 0
            for i in range(idx, n - p + 1):
                cur_sum += nums[i]
                max_partition_sum = max(cur_sum, helper(i + 1, p - 1))
                min_max_sum = min(min_max_sum, max_partition_sum)
                if cur_sum > min_max_sum:
                    break
            
            return min_max_sum
            
        return helper(0, k)