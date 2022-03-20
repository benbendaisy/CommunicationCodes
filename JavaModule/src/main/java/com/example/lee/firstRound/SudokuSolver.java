package com.example.lee.firstRound;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 2/6/15.
 *
 * Write a program to solve a Sudoku puzzle by filling the empty cells.
 *
 * Empty cells are indicated by the character '.'.
 *
 * You may assume that there will be only one unique solution.
 *
 *
 * A sudoku puzzle...
 * ...and its solution numbers marked in red.
 */
public class SudokuSolver {

    public void solveSudoku(char[][] board) {
        solveSudokuI(board);
    }
    public boolean solveSudokuI(char[][] board) {
        if (null == board || board.length != 9 || board[0].length != 9) {
            return false;
        }
        int row = board.length;
        int col = board[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == '.') {
                    for (int k = 1; k <= 9; k++) {
                        board[i][j] = (char) ('0' + k);
                        if (isValid(board, i, j) && solveSudokuI(board)) {
                            return true;
                        }
                        board[i][j] = '.';
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, int i, int j) {
        Set<Character> set = new HashSet<Character>();
        int row = board.length;
        int col = board[0].length;

        //check the ith row
        for (int k = 0; k < col; k++) {
            if (board[i][k] >= '0' && board[i][k] <= '9') {
                if (!set.add(board[i][k])) {
                    return false;
                }
            }
        }

        //check the jth colum
        set = new HashSet<Character>();
        for (int k = 0; k < row; k++) {
            if (board[k][j] >= '0' && board[k][j] <= '9') {
                if (!set.add(board[k][j])) {
                    return false;
                }
            }
        }

        //check submetrix
        //find the right start row and column
        int idx = i/3 * 3;
        int idy = j/3 * 3;

        set = new HashSet<Character>();
        for (int k = idx; k < idx + 3; k++) {
            for (int l = idy; l < idy + 3; l++) {
                if (board[k][l] >= '0' && board[k][l] <= '9') {
                    if (!set.add(board[k][l])) {
                        return false;
                    }
                }
            }
        }

        return true;

    }

    public static void main(String[] args) {
        Set<String> set = new HashSet<String>();
        set.add("Size=M");
        set.add("size=M");
        System.out.println(set);
    }

}
