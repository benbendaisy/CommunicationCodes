package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/11/15.
 */
public class SetMatrixZeroes {
    public void setZeroes(int[][] matrix) {
        if (null == matrix) return;
        int row = matrix.length;
        int col = matrix[0].length;
        boolean[] rows = new boolean[row];
        boolean[] cols = new boolean[col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rows[i] = true;
                    cols[j] = true;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            if (rows[i]) {
                for (int j = 0; j < col; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int j = 0; j < col; j++) {
            if (cols[j]) {
                for (int i = 0; i < row; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    public void setZeroesI(int[][] matrix) {
        if (null == matrix) return;
        int row = matrix.length;
        int col = matrix[0].length;
        boolean[] rows = new boolean[row];
        boolean[] cols = new boolean[col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rows[i] = true;
                    cols[j] = true;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (rows[i] || cols[j]) matrix[i][j] = 0;
            }
        }
    }
}
