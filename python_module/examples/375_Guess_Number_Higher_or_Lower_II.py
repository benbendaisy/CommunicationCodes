import math
from functools import lru_cache


class Solution:
    """
        We are playing the Guessing Game. The game will work as follows:

        I pick a number between 1 and n.
        You guess a number.
        If you guess the right number, you win the game.
        If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
        Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
        Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

        Example 1:

        Input: n = 10
        Output: 16
        Explanation: The winning strategy is as follows:
        - The range is [1,10]. Guess 7.
            - If this is my number, your total is $0. Otherwise, you pay $7.
            - If my number is higher, the range is [8,10]. Guess 9.
                - If this is my number, your total is $7. Otherwise, you pay $9.
                - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
                - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
            - If my number is lower, the range is [1,6]. Guess 3.
                - If this is my number, your total is $7. Otherwise, you pay $3.
                - If my number is higher, the range is [4,6]. Guess 5.
                    - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
                    - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
                    - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
                - If my number is lower, the range is [1,2]. Guess 1.
                    - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
                    - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
        The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
        Example 2:

        Input: n = 1
        Output: 0
        Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
        Example 3:

        Input: n = 2
        Output: 1
        Explanation: There are two possible numbers, 1 and 2.
        - Guess 1.
            - If this is my number, your total is $0. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $1.
        The worst case is that you pay $1.

        Constraints:

        1 <= n <= 200
    """
    def getMoneyAmount1(self, n: int) -> int:
        cache = {}
        def helper(s, e):
            if s >= e:
                return 0
            if (s, e) not in cache:
                t = math.inf
                for k in range(s, e + 1):
                    maxNextStep = max(helper(s, k - 1), helper(k + 1, e))
                    t = min(t, maxNextStep + k)
                cache[(s, e)] = t
            return cache[(s, e)]
        return helper(1, n)

    def getMoneyAmount(self, n: int) -> int:
        """
        passed leet code
        :param n:
        :return:
        """
        @lru_cache(None)
        def dfs(s, e):
            if s == e: return 0
            if s + 1 == e: return s
            temp = math.inf
            for k in range(s + 1, e):
                temp = min(temp, k + max(dfs(s, k - 1), dfs(k + 1, e)))
            return temp
        return dfs(1, n)


    def getMoneyAmount2(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = math.inf
                for k in range(i, j):
                    nextStep = max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], nextStep + k)
        return dp[1][n]

    def getMoneyAmount(self, n: int) -> int:
        @cache
        def helper(left: int, right: int):
            if left >= right:
                return 0
            
            min_cost = float("inf")
            for guess in range(left, right + 1):
                cost = guess + max(helper(left, guess - 1), helper(guess + 1, right))
                min_cost = min(min_cost, cost)
            return min_cost
        
        return helper(1, n)
