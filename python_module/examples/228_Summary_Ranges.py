from typing import List


class Solution:
    """
    You are given a sorted unique integer array nums.

    A range [a,b] is the set of all integers from a to b (inclusive).

    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
    
    Example 1:

    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"
    Example 2:

    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        prev = 0
        res = []
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                continue
            elif prev == i:
                res.append(str(nums[prev]))
            else:
                res.append(str(nums[prev]) + "->" + str(nums[i]))
            prev = i + 1
        return res