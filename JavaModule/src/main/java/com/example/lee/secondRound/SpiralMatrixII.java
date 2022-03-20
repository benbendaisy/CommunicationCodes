package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/26/15.
 */
public class SpiralMatrixII {
    public int[][] generateMatrix(int n) {
        if (n < 1) return new int[0][0];
        int len = n * n, idx = 0;
        int[][] matrix = new int[n][n];
        generateMatrix(matrix, 0, n - 1, 1);
        return matrix;
    }

    private void generateMatrix(int[][] matrix, int l, int r, int idx){
        int row = matrix.length;
        int col = matrix[0].length;
        if (idx > row * col || l > r) return;
        if (l == r) {
            matrix[l][l] = idx;
            return;
        }
        for (int j = l; j < r; j++) {
            matrix[l][j] = idx++;
        }
        for (int i = l; i < r; i++) {
            matrix[i][r] = idx++;
        }
        for (int j = r; j > l; j--) {
            matrix[r][j] = idx++;
        }
        for (int i = r; i > l; i--) {
            matrix[i][l] = idx++;
        }
        generateMatrix(matrix, l + 1, r - 1, idx);
    }
}
