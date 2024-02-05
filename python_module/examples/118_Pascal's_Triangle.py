from typing import List


class Solution:
    """
        Given an integer numRows, return the first numRows of Pascal's triangle.

        In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

        Example 1:

        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        Example 2:

        Input: numRows = 1
        Output: [[1]]
    """
    def generate1(self, numRows: int) -> List[List[int]]:
        triangle = []
        for r in range(numRows):
            row = [None for _ in range(r + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[r - 1][j - 1] + triangle[r - 1][j]
            triangle.append(row)
        return triangle
    
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        tri = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(tri[i - 1][j - 1] + tri[i - 1][j])
            row.append(1)
            tri.append(row)
        return tri
    
    def generate(self, numRows: int) -> List[List[int]]:
        def getRow(rowIndex: int) -> List[int]:
            @cache
            def get_num(row, col):
                if row == 0 or col == 0 or row == col:
                    return 1
                return get_num(row - 1, col - 1) + get_num(row - 1, col)
            ans = []
            for i in range(rowIndex + 1):
                ans.append(get_num(rowIndex, i))
            return ans
        ans = []
        for i in range(numRows):
            row = getRow(i)
            ans.append(row)
        return ans