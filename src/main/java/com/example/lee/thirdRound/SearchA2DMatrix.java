package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/15/17.
 */
public class SearchA2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int l = 0, r = matrix[0].length - 1;
        while (l < matrix.length && r >= 0) {
            if (matrix[l][r] == target) {
                return true;
            } else if (matrix[l][r] > target) {
                r--;
            } else {
                l++;
            }
        }
        return false;
    }
}
