from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        starting from left bottom
        :param matrix:
        :param target:
        :return:
        '''
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row > 0 and col < n:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        '''
        starting from top right
        :param matrix:
        :param target:
        :return:
        '''
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
        return False
