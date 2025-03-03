class Solution:
    """
    Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    Example 1:

    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4
    Example 2:


    Input: matrix = [["0","1"],["1","0"]]
    Output: 1
    Example 3:

    Input: matrix = [["0"]]
    Output: 0
    """
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        max_square = 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = []
            for i in range(n + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    length = min(h, w)
                    max_square = max(max_square, length ** 2)
                stack.append(i)
        return max_square
    
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
    
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        
        return max_side * max_side
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
    
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        max_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len