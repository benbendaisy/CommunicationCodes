class Solution:
    """
    You are given an array nums consisting of positive integers.

    We call a subarray of an array complete if the following condition is satisfied:

    The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
    Return the number of complete subarrays.

    A subarray is a contiguous non-empty part of an array.

    Example 1:

    Input: nums = [1,3,1,2,2]
    Output: 4
    Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
    Example 2:

    Input: nums = [5,5,5,5]
    Output: 10
    Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
    """
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_len = len(set(nums))
        freq = defaultdict(int)
        ans, unique_num, left, n = 0, 0, 0, len(nums)
        for right in range(n):
            num = nums[right]
            freq[num] += 1
            if freq[num] == 1:
                unique_num += 1
            while unique_num == unique_len:
                ans += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    unique_num -= 1
                left += 1
        return ans