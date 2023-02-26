class Solution:
    """
    Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

    Example 1:

    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].
    Example 2:

    Input: low = 8, high = 10
    Output: 1
    Explanation: The odd numbers between 8 and 10 are [9].
    """
    def countOdds1(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high + 1):
            if i % 2 != 0:
                cnt += 1
        return cnt

    def countOdds(self, low: int, high: int) -> int:
        # Initialize odd with the number of even numbers between low and high.
        cnt = (high - low) // 2
        # If either low or high is odd, increment odd by 1.
        if low % 2 == 1 or high % 2 == 1:
            cnt += 1
        return cnt
