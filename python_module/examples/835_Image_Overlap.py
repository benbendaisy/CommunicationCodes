from typing import List


class Solution:
    """
        You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

        We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

        Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

        Return the largest possible overlap.

        Example 1:

        Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
        Output: 3
        Explanation: We translate img1 to right by 1 unit and down by 1 unit.

        The number of positions that have a 1 in both images is 3 (shown in red).

        Example 2:

        Input: img1 = [[1]], img2 = [[1]]
        Output: 1
        Example 3:

        Input: img1 = [[0]], img2 = [[0]]
        Output: 0
    """
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dim = len(img1)
        def shift_and_count(xShift, yShift, M, R):
            """
                Shift the matrix M in up-left and up-right directions
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            left_shift_count, right_shift_count = 0, 0
            for rRow, mRow in enumerate(range(yShift, dim)):
                for rCol, mCol in enumerate(range(xShift, dim)):
                    if M[mRow][mCol] == 1 and M[mRow][mCol] == R[rRow][rCol]:
                        left_shift_count += 1
                    if M[mRow][rCol] == 1 and M[mRow][rCol] == R[rRow][mCol]:
                        right_shift_count += 1
            return max(left_shift_count, right_shift_count)

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, img1, img2))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, img2, img1))

        return max_overlaps


