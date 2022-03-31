from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and matrix[row][col] < target:
            if matrix[row][col] == target:
                return True
            row += 1

        while row < len(matrix) and col >= 0 and matrix[row][col] >= target:
            if matrix[row][col] == target:
                return True
            col -= 1

        return False

if __name__ == "__main__":
    matrix = [[1]]
    solution = Solution()
    ret = solution.searchMatrix(matrix, 3)
    print(ret)