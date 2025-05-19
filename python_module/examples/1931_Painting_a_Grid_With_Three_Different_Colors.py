class Solution:
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