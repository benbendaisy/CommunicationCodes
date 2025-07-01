class Solution:
    """
    Given a circular array nums, find the maximum absolute difference between adjacent elements.

    Note: In a circular array, the first and last elements are adjacent.

    Example 1:

    Input: nums = [1,2,4]

    Output: 3

    Explanation:

    Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

    Example 2:

    Input: nums = [-5,-10,-5]

    Output: 5

    Explanation:

    The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.
    """
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        def helper(arr: list[int]):
            max_diff = 0
            for i in range(len(arr) - 1):
                max_diff = max(max_diff, abs(arr[i] - arr[i + 1]))
            return max_diff
        
        return max(helper(nums), helper(nums[1:] + [nums[0]]))