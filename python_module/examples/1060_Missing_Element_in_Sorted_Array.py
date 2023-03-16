from typing import List


class Solution:
    """
        Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

        Example 1:

        Input: nums = [4,7,9,10], k = 1
        Output: 5
        Explanation: The first missing number is 5.
        Example 2:

        Input: nums = [4,7,9,10], k = 3
        Output: 8
        Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
        Example 3:

        Input: nums = [1,2,4], k = 3
        Output: 6
        Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
    """
    def missingElement1(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1] - 1
            if diff >= k:
                return nums[i - 1] + k
            else:
                k -= diff
        return nums[-1] + k
    def missingElement(self, nums: List[int], k: int) -> int:
        def calculate_missing(x):
            return nums[x] - nums[0] - x
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if calculate_missing(mid) < k:
                l = mid + 1
            else:
                r = mid
        return nums[0] + k + l - 1
