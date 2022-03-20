package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/11/15.
 */
public class Searcha2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (null == matrix) return false;
        int row = matrix.length;
        int col = matrix[0].length;
        int rdx = 0, cdx = col - 1;
        while (rdx < row && matrix[rdx][cdx] <= target) {
            if (matrix[rdx][cdx] == target) return true;
            rdx++;
        }
        if (rdx < row) {
            while (cdx >= 0 && matrix[rdx][cdx] >= target) {
                if (matrix[rdx][cdx] == target) return true;
                cdx--;
            }
        }
        return false;
    }
}
