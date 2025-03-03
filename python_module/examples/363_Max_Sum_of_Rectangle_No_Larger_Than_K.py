from bisect import bisect
from copy import deepcopy
from typing import List


class Solution:
    """
        Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

        It is guaranteed that there will be a rectangle with a sum no larger than k.

        Example 1:

        Input: matrix = [[1,0,1],[0,-2,3]], k = 2
        Output: 2
        Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
        Example 2:

        Input: matrix = [[2,2,-1]], k = 3
        Output: 3

        Constraints:

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 100
        -100 <= matrix[i][j] <= 100
        -105 <= k <= 105
    """
    @staticmethod
    def transpose(matrix):
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

    def maxSumSubmatrix1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) > len(matrix[0]):
            matrix = self.transpose(matrix)

        numRows = len(matrix)
        numCols = len(matrix[0])

        assert numCols >= numRows

        partialSumMatrix = deepcopy(matrix)

        for i in range(numRows):
            for j in range(numCols):
                if i > 0:         partialSumMatrix[i][j] += partialSumMatrix[i - 1][j]
                if j > 0:         partialSumMatrix[i][j] += partialSumMatrix[i][j - 1]
                if i > 0 and j > 0: partialSumMatrix[i][j] -= partialSumMatrix[i - 1][j - 1]

        # enumerate all first and last rows, then determine best among different cols
        ret = float("-inf")
        for firstRow in range(numRows):
            for lastRow in range(firstRow, numRows):
                sortedSums = [0]

                for j in range(numCols):
                    nextSum = partialSumMatrix[lastRow][j] - (partialSumMatrix[firstRow - 1][j] if firstRow > 0 else 0)
                    ind = bisect.bisect_left(sortedSums, nextSum - k)
                    if ind < len(sortedSums):
                        ret = max(ret, nextSum - sortedSums[ind])
                        if ret == k: # shortcut
                            return ret
                    bisect.insort(sortedSums, nextSum)

        return ret
    
    def maxSumSubmatrix2(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
    
        rows, cols = len(matrix), len(matrix[0])
        result = float('-inf')
        
        # For each possible left column
        for left in range(cols):
            # Initialize row sums for the current left boundary
            row_sums = [0] * rows
            
            # For each possible right column
            for right in range(left, cols):
                # Update row_sums to include the current column
                for i in range(rows):
                    row_sums[i] += matrix[i][right]
                
                # Find max subarray sum no more than k for the current set of columns
                # using prefix sums and a sorted list for efficient searching
                prefix_sum = 0
                sorted_sums = SortedList([0])  # Include 0 to handle full array sum
                
                for sum_val in row_sums:
                    prefix_sum += sum_val
                    # Find the smallest prefix sum y such that prefix_sum - y <= k
                    # This is equivalent to finding the smallest y where y >= prefix_sum - k
                    target = prefix_sum - k
                    idx = sorted_sums.bisect_left(target)
                    
                    if idx < len(sorted_sums):
                        result = max(result, prefix_sum - sorted_sums[idx])
                    
                    # Add current prefix sum to the sorted list
                    sorted_sums.add(prefix_sum)
                
        return result
    
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        res = float('-inf')

        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    row_sums[i] += matrix[i][right]
                
                prefix_sum = 0
                sorted_sums = SortedList([0])
                for val in row_sums:
                    prefix_sum += val
                    target = prefix_sum - k
                    idx = sorted_sums.bisect_left(target)
                    if idx < len(sorted_sums):
                        res = max(res, prefix_sum - sorted_sums[idx])
                    sorted_sums.add(prefix_sum)
        return res