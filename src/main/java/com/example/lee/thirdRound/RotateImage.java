package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/8/17.
 */
public class RotateImage {
    /**
     * key: matrix[i][j] = matrix[n-1-j][i]
     * @param matrix
     */
    public void rotate(int[][] matrix) {
        if (matrix == null || matrix.length != matrix[0].length) {
            return;
        }
        int n = matrix.length;
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < Math.ceil((double) n / 2); j++) {
                int t = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = t;
            }
        }
    }

    public static void main(String[] args) {
        System.out.println( 9 / 2);
        System.out.println( Math.ceil( (double) 9 / 2));
    }
}
