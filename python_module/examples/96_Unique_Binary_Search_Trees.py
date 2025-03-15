class Solution:
    """
    Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

    Example 1:

    Input: n = 3
    Output: 5
    Example 2:

    Input: n = 1
    Output: 1
    """
    def numTrees1(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            for i in range(1, nodes + 1):
                dp[nodes] += dp[i - 1] * dp[nodes - i]
        return dp[-1]
    
    def numberOfWays(self, numPeople: int) -> int:
        mod = 10**9 + 7
        n = numPeople // 2
        
        # Initialize dp array
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1  # Base case
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n] % mod