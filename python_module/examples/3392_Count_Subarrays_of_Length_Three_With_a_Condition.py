class Solution:
    """
    Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

    Example 1:

    Input: nums = [1,2,1,4,1]

    Output: 1

    Explanation:

    Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

    Example 2:

    Input: nums = [1,1,1]

    Output: 0

    Explanation:

    [1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.
    """
    def countSubarrays(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        
        running_sum, left = 0, 0
        cnt = 0
        for i, v in enumerate(nums):
            running_sum += v
            if i - left == 2:
                if 2 * (running_sum - nums[i - 1]) == nums[i - 1]:
                    cnt += 1
                running_sum -= nums[i - 2]
                left += 1
        return cnt