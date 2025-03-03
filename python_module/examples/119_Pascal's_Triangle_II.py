from typing import List


class Solution:
    """
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    Example 1:

    Input: rowIndex = 3
    Output: [1,3,3,1]
    Example 2:

    Input: rowIndex = 0
    Output: [1]
    Example 3:

    Input: rowIndex = 1
    Output: [1,1]
    """
    def getRow1(self, rowIndex: int) -> List[int]:
        @cache
        def get_num(row, col):
            if row == 0 or col == 0 or row == col:
                return 1
            return get_num(row - 1, col - 1) + get_num(row - 1, col)
        ans = []
        for i in range(rowIndex + 1):
            ans.append(get_num(rowIndex, i))
        return ans
    
    def getRow2(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        dp = [[0] * i for i in range(1, rowIndex + 1)]
        for i in range(rowIndex):
            dp[i][0] = 1
            dp[i][i] = 1
        
        for i in range(rowIndex):
            for j in range(i):
                if i != 0 and j != 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp[-1]
    
    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def get_row(row, col):
            if row == 0 or col == 0 or row == col:
                return 1
            
            return get_row(row - 1, col) + get_row(row - 1, col - 1)
        
        res = []
        for i in range(rowIndex + 1):
            res.append(get_row(rowIndex, i))
        return res