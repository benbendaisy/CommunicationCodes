from typing import List


class Solution:
    def generateMatrixRecursive(self, matrix: List[List[int]], val: int, it: int):
        if it > len(matrix)//2:
            return

        length = len(matrix)
        # the first row
        for j in range(it, length - it):
            matrix[it][j] = val
            val += 1

        # the right col
        for i in range(it + 1, length - it):
            matrix[i][length - it - 1] = val
            val += 1

        # the bottom row
        for j in range(length - it - 2, it, -1):
            matrix[length - it - 1][j] = val
            val += 1

        # the left col
        for i in range(length - it - 1, it, -1):
            matrix[i][it] = val
            val += 1

        self.generateMatrixRecursive(matrix, val, it + 1)

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        self.generateMatrixRecursive(matrix, 1, 0)
        return matrix

if __name__ == "__main__":
    n = 3
    solution = Solution()
    ret = solution.generateMatrix(n)
    print(ret)