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

    def generateMatrix1(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        self.generateMatrixRecursive(matrix, 1, 0)
        return matrix
    

    def generateMatrix2(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        num, row, col = 1, 0, 0
        direction = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        while num <= n*n:
            matrix[row][col] = num
            num += 1
            r_next = row + dx[direction]
            c_next = col + dy[direction]
            if r_next < 0 or r_next >= n or c_next < 0 or c_next >= n or matrix[r_next][c_next]!= 0:
                direction = (direction + 1) % 4
            row += dx[direction]
            col += dy[direction]
        return matrix
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        def generate_matrix(val, it):
            if it > len(matrix)//2:
                return

            # the first row
            for j in range(it, n - it):
                matrix[it][j] = val
                val += 1

            # the right col
            for i in range(it + 1, n - it):
                matrix[i][n - it - 1] = val
                val += 1

            # the bottom row
            for j in range(n - it - 2, it, -1):
                matrix[n - it - 1][j] = val
                val += 1

            # the left col
            for i in range(n - it - 1, it, -1):
                matrix[i][it] = val
                val += 1

            generate_matrix(val, it + 1)

        generate_matrix(1, 0)
        return matrix

if __name__ == "__main__":
    n = 3
    solution = Solution()
    ret = solution.generateMatrix(n)
    print(ret)