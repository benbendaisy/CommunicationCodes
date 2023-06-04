class Solution:
    """
    Alice plays the following game, loosely based on the card game "21".

    Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

    Alice stops drawing numbers when she gets k or more points.

    Return the probability that Alice has n or fewer points.

    Answers within 10-5 of the actual answer are considered accepted.

    Example 1:

    Input: n = 10, k = 1, maxPts = 10
    Output: 1.00000
    Explanation: Alice gets a single card, then stops.
    Example 2:

    Input: n = 6, k = 1, maxPts = 10
    Output: 0.60000
    Explanation: Alice gets a single card, then stops.
    In 6 out of 10 possibilities, she is at or below 6 points.
    Example 3:

    Input: n = 21, k = 17, maxPts = 10
    Output: 0.73278
    """
    def new21Game1(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        sum_window = 1.0
        prob = 0.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        for i in range(1, n + 1):
            dp[i] = sum_window / maxPts

            if i < k:
                sum_window += dp[i]
            else:
                prob += dp[i]
            
            if i >= maxPts:
                sum_window -= dp[i - maxPts]
        return prob
    
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, maxPts + 1):
                if i - j >= 0 and i - j < k:
                    dp[i] += dp[i - j] / maxPts
        return sum(dp[k:]) 
