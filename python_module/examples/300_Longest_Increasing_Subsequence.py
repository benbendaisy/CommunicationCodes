from bisect import bisect_left
from typing import List


class Solution:
    """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
        For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

        Example 1:

        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        Example 2:

        Input: nums = [0,1,0,3,2,3]
        Output: 4
        Example 3:

        Input: nums = [7,7,7,7,7,7,7]
        Output: 1

        Constraints:

        1 <= nums.length <= 2500
        -104 <= nums[i] <= 104
    """
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)
        dp = [1] * length

        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])

        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sub = []
        for num in nums:
            idx = bisect_left(sub, num)
            # If num is greater than any element in sub
            if idx == len(sub):
                sub.append(num)
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[idx] = num
        return len(sub)
    
    def lengthOfLIS3(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def lengthOfLIS4(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        return len(sub)
    
    def lengthOfLIS5(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = len(nums)
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def lengthOfLIS6(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def lengthOfLIS7(self, nums: List[int]) -> int:
        """
        Memory limit exceeded
        """
        if not nums:
            return 0
        n = len(nums)
        @cache
        def helper(idx: int, prev: int):
            if idx == n:
                return 0
            
            max_seq = helper(idx + 1, prev) # skip the current
            if prev == -1 or nums[idx] > nums[prev]:
                max_seq = max(max_seq, 1 + helper(idx + 1, idx))
            return max_seq
        return helper(0, -1)
    
    def lengthOfLIS8(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        @cache
        def helper(idx: int, prev_idx: int) -> int:
            if idx == n:
                return 0  # Base case: reached end of array

            # Option 1: Skip current element
            max_seq = helper(idx + 1, prev_idx)

            # Option 2: Include current element if it's increasing
            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                max_seq = max(max_seq, 1 + helper(idx + 1, idx))

            return max_seq

        return helper(0, -1)
