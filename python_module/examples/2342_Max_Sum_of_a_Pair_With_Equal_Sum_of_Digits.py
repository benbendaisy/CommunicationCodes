class Solution:
    """
    You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

    Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

    Example 1:

    Input: nums = [18,43,36,13,7]
    Output: 54
    Explanation: The pairs (i, j) that satisfy the conditions are:
    - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
    - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
    So the maximum sum that we can obtain is 54.
    Example 2:

    Input: nums = [10,12,19,14]
    Output: -1
    Explanation: There are no two numbers that satisfy the conditions, so we return -1.
    """
    def maximumSum(self, nums: List[int]) -> int:
        num_dict = defaultdict(list)
        def calculate_digit_sum(num: int):
            t = num
            local_sum = 0
            while t > 0:
                local_sum += t % 10
                t = t // 10
            return local_sum
        for num in nums:
            num_dict[calculate_digit_sum(num)].append(num)
        max_value = -1
        for _, value in num_dict.items():
            if len(value) < 2:
                continue
            value.sort()
            if value[-1] + value[-2] > max_value:
                max_value = value[-1] + value[-2]
        return max_value