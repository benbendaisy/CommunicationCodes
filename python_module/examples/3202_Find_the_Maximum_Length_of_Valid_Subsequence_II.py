class Solution:
    """
    You are given an integer array nums and a positive integer k.
    A subsequence sub of nums with length x is called valid if it satisfies:

    (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
    Return the length of the longest valid subsequence of nums.

    Example 1:

    Input: nums = [1,2,3,4,5], k = 2

    Output: 5

    Explanation:

    The longest valid subsequence is [1, 2, 3, 4, 5].

    Example 2:

    Input: nums = [1,4,2,3,1,4], k = 3

    Output: 4

    Explanation:

    The longest valid subsequence is [1, 4, 1, 4].
    """
    def maximumLength1(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        @cache
        def helper(idx: int, pre_sum: int, pre_num: int, length: int):
            if idx == n:
                return length
            
            # option 1: skip the num
            opt1 = helper(idx + 1, pre_sum, pre_num, length)

            # option 2: take the num
            # append it to the seq
            if (nums[idx] + pre_num) % k == pre_sum:
                opt2 = helper(idx + 1, pre_sum, nums[idx], length + 1)
            else:
                # restart the seq
                opt2 = helper(idx + 1, (nums[idx] + pre_num) % k, nums[idx], 2)
            return max(opt1, opt2)
        
        return helper(1, -1, nums[0], 0)
    
    def maximumLength2(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res