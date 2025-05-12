class Solution:
    """
    You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

    Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

    In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

    Example 1:

    Input: n = 3
    Output: 5
    Explanation: The five different ways are show above.
    Example 2:

    Input: n = 1
    Output: 1
    """
    def numTilings1(self, n: int) -> int:
        # Define modulo value
        mod = 10**9 + 7
        
        # Handle base cases
        if n <= 2:
            return n
        
        # Define three states:
        # dp[i][0]: board filled up to column i, with no protrusion
        # dp[i][1]: board filled up to column i, with protrusion in top row
        # dp[i][2]: board filled up to column i, with protrusion in bottom row
        dp = [[0, 0, 0] for _ in range(n + 1)]
        
        # Base cases
        dp[0][0] = 1  # Empty board, one way to tile (do nothing)
        dp[1][0] = 1  # Fill a 2×1 board with a single domino
        
        # Fill dp table
        for i in range(2, n + 1):
            # Case 1: No protrusion in previous state
            # - Add a vertical domino
            # - Add two horizontal dominos
            # - Add two trominos
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]) % mod
            
            # Case 2: Protrusion in top row from previous state
            # - Add a horizontal domino to cover the protrusion
            # - Add a tromino to cover the protrusion
            dp[i][1] = (dp[i-2][0] + dp[i-1][2]) % mod
            
            # Case 3: Protrusion in bottom row from previous state
            # - Add a horizontal domino to cover the protrusion
            # - Add a tromino to cover the protrusion
            dp[i][2] = (dp[i-2][0] + dp[i-1][1]) % mod
        
        # The answer is the number of ways to tile the entire board with no protrusion
        return dp[n][0]
    
    def numTilings2(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @cache  
        def p(n):  
            if n == 2:
                return 1
            return (p(n - 1) + f(n - 2)) % mod

        @cache  
        def f(n):  
            if n <= 2:
                return n
            return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % mod

        return f(n)
    
    def numTilings3(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
    
    def numTilings4(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def part(m):
            if m == 2:
                return 1
            return (part(m - 1) + full(m - 2)) % mod
        @cache
        def full(m):
            if m <= 2:
                return m
            return (full(m - 1) + full(m - 2) + 2 * part(m - 1)) % mod
        return full(n)
    
    def numTilings5(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod
        return dp[n]