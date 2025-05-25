class Solution:
    """
    You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

    Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

    Example 1:

    Input: m = 1, n = 1
    Output: 3
    Explanation: The three possible colorings are shown in the image above.
    Example 2:


    Input: m = 1, n = 2
    Output: 6
    Explanation: The six possible colorings are shown in the image above.
    Example 3:

    Input: m = 5, n = 5
    Output: 580986
    """
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        colors = [0, 1, 2]  # 0: Red, 1: Green, 2: Blue

        # Step 1: Generate all valid column states
        @lru_cache(None)
        def valid_columns():
            valid = []
            for col in product(colors, repeat=m):
                if all(col[i] != col[i+1] for i in range(m - 1)):
                    valid.append(col)
            return valid

        valid = valid_columns()

        # Step 2: Build transition graph between valid columns
        transitions = {}
        for c1 in valid:
            transitions[c1] = []
            for c2 in valid:
                if all(a != b for a, b in zip(c1, c2)):
                    transitions[c1].append(c2)

        # Step 3: DP over n columns
        dp = {}
        for state in valid:
            dp[state] = 1  # Base case: 1st column

        for _ in range(n - 1):
            new_dp = {}
            for curr in valid:
                new_dp[curr] = 0
                for prev in transitions[curr]:
                    new_dp[curr] = (new_dp[curr] + dp[prev]) % mod
            dp = new_dp

        return sum(dp.values()) % mod