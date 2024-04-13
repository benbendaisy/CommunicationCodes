from pyparsing import List


class Solution:
    """
    Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

    Example 1:

    Input: nums = [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
    Example 2:

    Input: nums = [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
    """
    def findMaxLength(self, nums: List[int]) -> int:
        cnt_map = {0:-1}
        max_len = cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt -= 1
            if cnt in cnt_map:
                max_len = max(max_len, i - cnt_map.get(cnt))
            else:
                cnt_map[cnt] = i
        return max_len