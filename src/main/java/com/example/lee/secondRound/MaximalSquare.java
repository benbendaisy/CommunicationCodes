package com.example.lee.secondRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 6/4/15.
 *
 * Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
 *
 * For example, given the following matrix:
 *
 * 1 0 1 0 0
 * 1 0 1 1 1
 * 1 1 1 1 1
 * 1 0 0 1 0
 * Return 4.
 *
 *
 */
public class MaximalSquare {
    public int maximalSquare(char[][] matrix) {
        if (null == matrix || matrix.length == 0) return 0;
        int row = matrix.length;
        int col = matrix[0].length;
        int[] h = new int[col];
        int[] l = new int[col];
        int[] r = new int[col];
        int max = 0;
        Arrays.fill(r, col);
        for (int i = 0; i < row; i++) {
            int left = 0;
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    h[j]++;
                    l[j] = Math.max(l[j], left);
                } else {
                    l[j] = 0;
                    h[j] = 0;
                    r[j] = col;
                    left = j + 1;
                }
            }

            int right = col;
            for (int j = col - 1; j >= 0; j--) {
                if (matrix[i][j] == '1') {
                    r[j] = Math.min(r[j], right);
                    int len = Math.min(r[j] - l[j], h[j]);
                    max = Math.max(max, len * len);
                } else {
                    right = j;
                }
            }
        }
        return max;
    }
}
