class Solution:
    """
    You are given an integer array nums.
    A subsequence sub of nums with length x is called valid if it satisfies:

    (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
    Return the length of the longest valid subsequence of nums.

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    Example 1:

    Input: nums = [1,2,3,4]

    Output: 4

    Explanation:

    The longest valid subsequence is [1, 2, 3, 4].

    Example 2:

    Input: nums = [1,2,1,1,2,1,2]

    Output: 6

    Explanation:

    The longest valid subsequence is [1, 2, 1, 2, 1, 2].

    Example 3:

    Input: nums = [1,3]

    Output: 2

    Explanation:

    The longest valid subsequence is [1, 3].
    """
    def maximumLength1(self, nums: List[int]) -> int:
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
            if (nums[idx] + pre_num) % 2 == pre_sum:
                opt2 = helper(idx + 1, pre_sum, nums[idx], length + 1)
            else:
                # restart the seq
                opt2 = helper(idx + 1, (nums[idx] + pre_num) % 2, nums[idx], 2)
            return max(opt1, opt2)
        
        return helper(1, -1, nums[0], 0)
    
    def maximumLength2(self, nums: List[int]) -> int:
        res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res