import heapq
from collections import defaultdict
from typing import List


class Solution:
    """
        A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

        Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

        Example 1:

        Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
        Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
        Example 2:

        Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
        Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

        Constraints:

        m == mat.length
        n == mat[i].length
        1 <= m, n <= 100
        1 <= mat[i][j] <= 100
    """
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Store the matrix dimensions
        m, n = len(mat), len(mat[0])

        # Hash Map to store the diagonals. We will use a list
        # for now, but then heapify each list before taking them out.
        diagonals = defaultdict(list)

        # Insert values into the Hash Map.
        for row in range(m):
            for col in range(n):
                # Observing that on each diagonal, the differences between the row and column indices
                # of each element is the same.
                # Hence we can use row - col as the key to collect elements on the same diagonal.
                diagonals[row - col].append(mat[row][col])

        # Heapify each list in the Hash Map.
        for diagonal in diagonals.values():
            heapq.heapify(diagonal)

        # Take values back out of the Hash Map.
        for row in range(m):
            for col in range(n):
                mat[row][col] = heapq.heappop(diagonals[row - col])

        return mat

