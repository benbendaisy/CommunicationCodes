package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/27/15.
 *
 * Follow up for N-Queens problem.
 *
 * Now, instead outputting board configurations, return the total number of distinct solutions.
 */
public class NQueensII {
    public int totalNQueens(int n) {
        if(n <= 0){
            return 0;
        }

        int[] columns = new int[n];
        return totalNQueens(n, columns, 0);
    }

    private int totalNQueens(int n, int[] columns, int row){
        if(row == n){
            return 1;
        }

        int count = 0;

        for(int i = 0; i < n; i++){
            if(canPlaceQueen(row, columns, i)){
                columns[row] = i;
                count += totalNQueens(n, columns, row + 1);
            }
        }

        return count;
    }

    private boolean canPlaceQueen(int row, int[] columns, int column){
        for(int i = 0; i < row; i++){
            if(column == columns[i] || Math.abs(row - i) == Math.abs(columns[i] - column)){
                return false;
            }
        }
        return true;
    }
}
