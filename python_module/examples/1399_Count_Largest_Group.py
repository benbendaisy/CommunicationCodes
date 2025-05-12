class Solution:
    """
    You are given an integer n.

    Each number from 1 to n is grouped according to the sum of its digits.

    Return the number of groups that have the largest size.

    Example 1:

    Input: n = 13
    Output: 4
    Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
    [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
    There are 4 groups with largest size.
    Example 2:

    Input: n = 2
    Output: 2
    Explanation: There are 2 groups [1], [2] of size 1.
    """
    def countLargestGroup1(self, n: int) -> int:
        def sum_digits(num_str: int):
            digits = list(map(int, list(str(num_str))))
            return sum(digits)
        freq = defaultdict(int)
        for i in range(1, n + 1):
            freq[sum_digits(i)] += 1
        cnt = 0
        max_values = max(freq.values())
        for k, v in freq.items():
            if v == max_values:
                cnt += 1
        return cnt
    
    def countLargestGroup(self, n: int) -> int:
        freq = defaultdict(int)
        max_freq = 0
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            freq[digit_sum] += 1
            max_freq = max(max_freq, freq[digit_sum])
        
        return sum(1 for _, v in freq.items() if v == max_freq)