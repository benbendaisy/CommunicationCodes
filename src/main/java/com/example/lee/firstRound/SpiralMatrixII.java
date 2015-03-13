package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/23/15.
 *
 * Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
 *
 * For example,
 * Given n = 3,
 *
 * You should return the following matrix:
 * [
 * [ 1, 2, 3 ],
 * [ 8, 9, 4 ],
 * [ 7, 6, 5 ]
 * ]
 */
public class SpiralMatrixII {
    public int[][] generateMatrix(int n) {
        if(n <= 0){
            return new int[0][0];
        }
        int[][] matrix = new int[n][n];

        int count = 1;
        int round = n / 2;
        int level = 0;

        while(round > 0){
            for(int j = level; j < n - level; j++){
                matrix[level][j] = count;
                count++;
            }
            for(int i = level + 1; i < n - level; i++){
                matrix[i][n - level - 1] = count;
                count++;
            }
            for(int j = n-level - 2; j >= level; j--){
                matrix[n - level - 1][j] = count;
                count++;
            }
            for(int i = n - level - 2; i >= level + 1; i--){
                matrix[i][level] = count;
                count++;
            }
            round--;
            level++;
        }

        if(n % 2 != 0){
            matrix[level][level] = count;
        }
        return matrix;
    }

    public static void main(String[] args) {
        SpiralMatrixII spiralMatrixII = new SpiralMatrixII();
        int[][] matrix = spiralMatrixII.generateMatrix(3);
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                System.out.print(matrix[i][j] + " ");
            }
            System.out.print("\n");
        }
    }
}
