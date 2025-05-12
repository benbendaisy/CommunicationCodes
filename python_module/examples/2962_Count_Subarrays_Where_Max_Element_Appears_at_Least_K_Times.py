class Solution:
    """
    You are given an integer array nums and a positive integer k.

    Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

    A subarray is a contiguous sequence of elements within an array.

    Example 1:

    Input: nums = [1,3,2,3,3], k = 2
    Output: 6
    Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
    Example 2:

    Input: nums = [1,4,2,1], k = 3
    Output: 0
    Explanation: No subarray contains the element 4 at least 3 times.
    """
    def countSubarrays1(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left, n = 0, len(nums)
        max_element = max(nums)
        res, max_element_cnt = 0, 0
        for right in range(n):
            if nums[right] == max_element:
                max_element_cnt += 1
            while max_element_cnt == k:
                if nums[left] == max_element:
                    max_element_cnt -= 1
                left += 1
            res += left
        return res
    
    def countSubarrays2(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        max_cnt, cnt, left = 0, 0, 0
        max_num, n = max(nums), len(nums)
        for i, num in enumerate(nums):
            if num == max_num:
                max_cnt += 1
            while max_cnt == k:
                if nums[left] == max_num:
                    max_cnt -= 1
                left += 1
            cnt += left
        return cnt
    
    def countSubarrays3(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        max_cnt, cnt, left = 0, 0, 0
        max_num, n = max(nums), len(nums)
        for i, num in enumerate(nums):
            if num == max_num:
                max_cnt += 1
            while max_cnt >= k:
                if nums[left] == max_num:
                    max_cnt -= 1
                left += 1
                cnt += n - i
        return cnt
