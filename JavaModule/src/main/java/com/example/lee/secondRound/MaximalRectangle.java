package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/24/15.
 */
public class MaximalRectangle {
    public int maximalRectangle(char[][] matrix) {
        if (null == matrix || matrix.length == 0) return 0;
        int row = matrix.length;
        int col = matrix[0].length;
        int[] l = new int[col];
        int[] r = new int[col];
        int[] h = new int[col];
        for (int i = 0; i < col; i++) {
            r[i] = col;
        }
        int max = 0;
        for (int i = 0; i < row; i++) {
            int left = 0;
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    l[j] = Math.max(l[j], left);
                    h[j]++;
                } else {
                    l[j] = 0;
                    r[j] = col;
                    h[j] = 0;
                    left = j + 1;
                }
            }

            int right = col;
            for (int j = col - 1; j >= 0; j--) {
                if (matrix[i][j] == '1') {
                    r[j] = Math.min(right, r[j]);
                    max = Math.max(max, (r[j] - l[j]) * h[j]);
                } else {
                    right = j;
                }
            }
        }
        return max;
    }
}
