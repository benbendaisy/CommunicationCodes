class Solution:
    """
    You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

    Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

    Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

    Example 1:

    Input: rowSum = [3,8], colSum = [4,7]
    Output: [[3,0],
            [1,7]]
    Explanation: 
    0th row: 3 + 0 = 3 == rowSum[0]
    1st row: 1 + 7 = 8 == rowSum[1]
    0th column: 3 + 1 = 4 == colSum[0]
    1st column: 0 + 7 = 7 == colSum[1]
    The row and column sums match, and all matrix elements are non-negative.
    Another possible matrix is: [[1,2],
                                [3,5]]
    Example 2:

    Input: rowSum = [5,7,10], colSum = [8,6,8]
    Output: [[0,5,0],
            [6,1,0],
            [2,0,8]]
    """
    def restoreMatrix1(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]  # Initialize matrix with zeros
        
        # Fill the matrix greedily
        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i], colSum[j])  # Assign the smallest possible value
                rowSum[i] -= matrix[i][j]  # Deduct from row sum
                colSum[j] -= matrix[i][j]  # Deduct from column sum
        
        return matrix
    
    def restoreMatrix2(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        ttl
        """
        max_num = max(max(rowSum), max(colSum))
        m, n = len(rowSum), len(colSum)
        def check_matrix(matrix: List[List[int]]):
            for i, row in enumerate(matrix):
                if sum(row) != rowSum[i]:
                    return False
            
            for j in range(n):
                col_sum = 0
                for i in range(m):
                    col_sum += matrix[i][j]
                if col_sum != colSum[j]:
                    return False

            return True

        def back_track(row: int, col: int):
            if row == m:
                if check_matrix(matrix):
                    return True
                return False
            
            t = matrix[row][col]
            for k in range(0, max_num + 1):
                matrix[row][col] = k
                next_row, next_col = (row + 1, 0) if col == n - 1 else (row, col + 1)
                if back_track(next_row, next_col):
                    return True
                matrix[row][col] = t
                    
            return False
        matrix = [[0] * n for _ in range(m)]
        back_track(0, 0)
        return matrix

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        def back_track(row, col):
            if row == m:
                return True
            
            next_row, next_col = (row + 1, 0) if col == n - 1 else (row, col + 1)
            matrix[row][col] = min(rowSum[row], colSum[col])

            rowSum[row] -= matrix[row][col]
            colSum[col] -= matrix[row][col]

            if back_track(next_row, next_col):
                return True
            
            rowSum[row] += matrix[row][col]
            colSum[col] += matrix[row][col]
            matrix[row][col] = 0

            return False
        back_track(0, 0)
        return matrix