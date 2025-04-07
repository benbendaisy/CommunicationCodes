class Solution:
    """
    You are given a 0-indexed integer array nums and a positive integer k.

    We call an index i k-big if the following conditions are satisfied:

    There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
    There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
    Return the number of k-big indices.

    Example 1:

    Input: nums = [2,3,6,5,2,3], k = 2
    Output: 2
    Explanation: There are only two 2-big indices in nums:
    - i = 2 --> There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
    - i = 3 --> There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.
    Example 2:

    Input: nums = [1,1,1], k = 3
    Output: 0
    Explanation: There are no 3-big indices in nums.
    """
    def kBigIndices1(self, nums: List[int], k: int) -> int:
        """
        Time limit exceeded for large test cases.
        """
        if not nums or len(nums) <= k:
            return 0
        n, k_cnt = len(nums), 0
        for i in range(k, n - k):
            cnt = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    cnt += 1
            if cnt < k:
                continue
            cnt = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    cnt += 1
            if cnt >= k:
                k_cnt += 1
        return k_cnt
    
    def kBigIndices2(self, nums: List[int], k: int) -> int:
        left_smaller = [0] * len(nums)
        right_smaller = [0] * len(nums)
        
        sorted_list = SortedList()
        for i in range(len(nums)):
            left_smaller[i] = sorted_list.bisect_left(nums[i])
            sorted_list.add(nums[i])
        
        sorted_list.clear()
        for i in range(len(nums) - 1, -1, -1):
            right_smaller[i] = sorted_list.bisect_left(nums[i])
            sorted_list.add(nums[i])
        
        count = 0
        for i in range(len(nums)):
            if left_smaller[i] >= k and right_smaller[i] >= k:
                count += 1
        
        return count
            