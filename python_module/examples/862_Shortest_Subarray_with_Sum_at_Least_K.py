class Solution:
    """
    Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

    A subarray is a contiguous part of an array.

    Example 1:

    Input: nums = [1], k = 1
    Output: 1
    Example 2:

    Input: nums = [1,2], k = 4
    Output: -1
    Example 3:

    Input: nums = [2,-1,2], k = 3
    Output: 3
    """
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        length = len(nums)
        pre_sum = [0] + list(accumulate(nums))
        que = collections.deque()
        min_length = float('inf')
        for i in range(length + 1):
            while que and pre_sum[i] - pre_sum[que[0]] >= k:
                min_length = min(min_length, i - que.popleft())
            while que and pre_sum[i] <= pre_sum[que[-1]]:
                que.pop()
            que.append(i)
        return -1 if min_length == float('inf') else min_length