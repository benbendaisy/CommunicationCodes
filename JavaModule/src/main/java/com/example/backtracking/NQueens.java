package com.example.backtracking;

/**
 * Created by benbendaisy on 5/22/15.
 */
public class NQueens {
    private boolean isSafe(int[] columns, int row, int column) {
        for (int i = 0; i < row; i++) {
            if (columns[i] == column || row - i == Math.abs(column - columns[i])) return false;
        }
        return true;
    }

    public boolean solveNQueens(int[][] board, int[] columns, int row) {
        if (row == board.length) return true;
        for (int i = 0; i < board.length; i++) {
            if (isSafe(columns, row, i)) {
                board[row][i] = 1;
                columns[row] = i;
                if (solveNQueens(board, columns, row + 1)) return true;
                board[row][i] = 0;
                columns[row] = -1;
            }
        }
        return false;
    }
}
