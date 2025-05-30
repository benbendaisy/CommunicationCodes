class Solution:
    """
    There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

    Serve 100 ml of soup A and 0 ml of soup B,
    Serve 75 ml of soup A and 25 ml of soup B,
    Serve 50 ml of soup A and 50 ml of soup B, and
    Serve 25 ml of soup A and 75 ml of soup B.
    When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

    Note that we do not have an operation where all 100 ml's of soup B are used first.

    Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

    Example 1:

    Input: n = 50
    Output: 0.62500
    Explanation: If we choose the first two operations, A will become empty first.
    For the third operation, A and B will become empty at the same time.
    For the fourth operation, B will become empty first.
    So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
    Example 2:

    Input: n = 100
    Output: 0.71875
    """
    def soupServings1(self, n: int) -> float:
        @lru_cache(None)
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            return 0.25 * (dfs(a-100, b) + dfs(a-75, b-25) + dfs(a-50, b-50) + dfs(a-25, b-75))
        return 1 if n > 4450 else dfs(n, n)
    
    def soupServings2(self, n: int) -> float:
        if n > 5000:
            return 1.0  # Approximates to 1 for large n due to diminishing returns
        
        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            return 0.25 * (dp(a - 100, b) + dp(a - 75, b - 25) + dp(a - 50, b - 50) + dp(a - 25, b - 75))
        
        return dp(n, n)
    
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0
        
        @cache
        def helper(x, y):
            if x <= 0 and y <= 0:
                return 0.5
            if x <= 0:
                return 1.0
            if y <= 0:
                return 0.0
            
            return 0.25 * (helper(x - 100, y) + helper(x - 75, y - 25) + helper(x - 50, y - 50) + helper(x - 25, y - 75))
        
        return helper(n, n)
