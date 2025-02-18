class Solution:
    """
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Example 1:

    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
    Example 2:

    Input: nums = [1,0,1,1,0,1]
    Output: 2

    Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_cnt, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0
        return max_cnt