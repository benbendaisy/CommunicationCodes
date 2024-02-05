from collections import defaultdict
from typing import List


class Solution:
    """
        Given a matrix and a target, return the number of non-empty submatrices that sum to target.

        A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

        Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

        Example 1:

        Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
        Output: 4
        Explanation: The four 1x1 submatrices that only contain 0.
        Example 2:

        Input: matrix = [[1,-1],[-1,1]], target = 0
        Output: 5
        Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
        Example 3:

        Input: matrix = [[904]], target = 0
        Output: 0

        Constraints:

        1 <= matrix.length <= 100
        1 <= matrix[0].length <= 100
        -1000 <= matrix[i] <= 1000
        -10^8 <= target <= 10^8
    """
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        ds = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ds[i][j] = ds[i - 1][j] + ds[i][j - 1] - ds[i - 1][j - 1] + matrix[i - 1][j - 1]

        cnt = 0
        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):
                h = defaultdict(int)
                h[0] = 1
                for col in range(1, c + 1):
                    # 1d subarray
                    currSum = ds[r2][col] - ds[r1 - 1][col]
                    # sum of 1d subarrays
                    cnt += h[currSum - target]
                    # save current prefix sum
                    h[currSum] += 1
        return cnt
    
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]
        cnt = 0
        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):
                h = defaultdict(int)
                h[0] = 1
                for col in range(1, c + 1):
                    cur_sum = ps[r2][col] - ps[r1 - 1][col]
                    cnt += h[cur_sum - target]
                    h[cur_sum] += 1
        return cnt

