class Solution:
    """
    Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

    A subarray is a contiguous part of the array.

    Example 1:

    Input: nums = [1,0,1,0,1], goal = 2
    Output: 4
    Explanation: The 4 subarrays are bolded and underlined below:
    [1,0,1,0,1]
    [1,0,1,0,1]
    [1,0,1,0,1]
    [1,0,1,0,1]
    Example 2:

    Input: nums = [0,0,0,0,0], goal = 0
    Output: 15
    """
    def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:
        total_cnt, cur_sum = 0, 0
        freq = defaultdict(int)
        for num in nums:
            cur_sum += num
            if cur_sum == goal:
                total_cnt += 1
            if cur_sum - goal in freq:
                total_cnt += freq[cur_sum - goal]
            freq[cur_sum] += 1
        return total_cnt
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sliding_window_at_most(cur_goal):
            start, cur_sum, total_cnt = 0, 0, 0
            for end in range(len(nums)):
                cur_sum += nums[end]
                while start <= end and cur_sum > cur_goal:
                    cur_sum -= nums[start]
                    start += 1
                total_cnt += end - start + 1
            return total_cnt
        return sliding_window_at_most(goal) - sliding_window_at_most(goal - 1)