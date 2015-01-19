package com.example.lee;

/**
 * Created by benbendaisy on 1/17/15.
 *
 * Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
 */
public class SetMatrixZeroes {
    //O(m * n) space
    public void setZeroes(int[][] matrix) {
        if(matrix == null){
            return;
        }

        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0 && !visited[i][j]){
                    setRowColumnZeros(matrix, i, j, visited);
                }
            }
        }
    }

    private void setRowColumnZeros(int[][] matrix, int i, int j, boolean[][] visited){
        for(int k = 0; k < matrix[0].length; k++){
            if(matrix[i][k] != 0){
                matrix[i][k] = 0;
                visited[i][k] = true;
            }
        }
        for(int k = 0; k < matrix.length; k++){
            if(matrix[k][j] != 0){
                matrix[k][j] = 0;
                visited[k][j] = true;
            }
        }
    }

    //o(m+n) space
    public void setZeroesI(int[][] matrix) {
        if(matrix == null){
            return;
        }

        //check if first row and column has zeros;
        boolean[] rows = new boolean[matrix.length];
        boolean[] cols = new boolean[matrix[0].length];

        //mark first row and column to zero if there is zero in that row and column
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    rows[i] = true;
                    cols[j] = true;
                }
            }
        }

        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(rows[i] || cols[j]){
                    matrix[i][j] = 0;
                }
            }
        }
    }

    //save zero information to first row and column
    public void setZeroesII(int[][] matrix) {
        if(matrix == null){
            return;
        }

        //check if first row and column has zeros;
        boolean isFirstRowHasZero = false, isFirstColumnHasZero = false;
        for(int i = 0; i < matrix.length; i++){
            if(matrix[i][0] == 0){
                isFirstColumnHasZero = true;
                break;
            }
        }
        for(int j = 0; j < matrix[0].length; j++){
            if(matrix[0][j] == 0){
                isFirstRowHasZero = true;
            }
        }

        //mark first row and column to zero if there is zero in that row and column
        for(int i = 1; i < matrix.length; i++){
            for(int j = 1; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for(int i = 1; i < matrix.length; i++){
            for(int j = 1; j < matrix[0].length; j++){
                if(matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
        }

        if(isFirstRowHasZero){
            for(int j = 0; j < matrix[0].length; j++){
                matrix[0][j] = 0;
            }
        }

        if(isFirstColumnHasZero){
            for(int i = 0; i < matrix.length; i++){
                matrix[i][0] = 0;
            }
        }

    }
}
