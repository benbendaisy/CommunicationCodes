package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/9/17.
 */
public class SpiralMatrixII {
    public int[][] generateMatrix(int n) {
        if (n < 1) {
            return new int[0][0];
        }
        double len = Math.ceil((double) n / 2);
        int idx = 1;
        int[][] metrix = new int[n][n];
        for (int i = 0; i < len; i++) {
            // top row
            for (int j = i; j < n - i; j++) {
                metrix[i][j] = idx++;
            }
            // single row
            if (i >= n - i - 1) {
                break;
            }

            // right column
            for (int j = i + 1; j < n - i; j++) {
                metrix[j][n - i - 1] = idx++;
            }

            // bottom row
            for (int j = n - i - 2; j >= i; j--) {
                metrix[n - i - 1][j] = idx++;
            }

            // left column
            for (int j = n - i - 2; j > i; j--) {
                metrix[j][i] = idx++;
            }
        }
        return metrix;
    }

    public static void main(String[] args) {
        SpiralMatrixII spiralMatrixII = new SpiralMatrixII();
        int[][] metrix = spiralMatrixII.generateMatrix(5);
        System.out.println();
    }
}
