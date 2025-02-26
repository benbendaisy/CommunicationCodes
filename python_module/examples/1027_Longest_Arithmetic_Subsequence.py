class Solution:
    """
    Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

    Note that:

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
    A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
    
    Example 1:

    Input: nums = [3,6,9,12]
    Output: 4
    Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
    Example 2:

    Input: nums = [9,4,7,2,10]
    Output: 3
    Explanation:  The longest arithmetic subsequence is [4,7,10].
    Example 3:

    Input: nums = [20,1,15,3,10,5,8]
    Output: 4
    Explanation:  The longest arithmetic subsequence is [20,15,10,5].
    """
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        # If array has 1 or 2 elements, that's the longest sequence
        if n <= 2:
            return n
        # dp[i][diff] will store the length of arithmetic subsequence ending at index i
        # with difference 'diff'
        dp = [{} for _ in range(n)]
        # Minimum length of an arithmetic sequence is 2
        max_len = 2
        for i in range(n):
            for j in range(i):
                # Calculate the difference between current and previous elements
                diff = nums[i] - nums[j]
                # If we've seen a subsequence ending at index j with the same difference,
                # extend it by adding nums[i]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    # Start a new subsequence with just these two elements
                    dp[i][diff] = 2
                # Update the maximum length
                max_len = max(max_len, dp[i][diff])
        return max_len