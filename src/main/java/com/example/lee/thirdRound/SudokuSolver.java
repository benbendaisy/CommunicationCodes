package com.example.lee.thirdRound;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 7/6/17.
 */
public class SudokuSolver {
    public void solveSudoku(char[][] board) {
        if (board == null || board.length != 9 || board[0].length != 9) {
            return;
        }
        solveSudokuHelper(board);
    }

    private boolean solveSudokuHelper(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == '.') {
                    for (int k = 1; k <= 9; k++) {
                        board[i][j] = (char) ('0' + k);
                        if (isValid(board, i, j) && solveSudokuHelper(board)) {
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
        Set<Character> seenCharacter = new HashSet<>();
        // check row
        for (int k = 0; k < board[0].length; k++) {
            if (board[i][k] >= '1' && board[i][k] <= '9' && !seenCharacter.add(board[i][k])) {
                return false;
            }
        }

        // check column
        seenCharacter.clear();
        for (int k = 0; k < board.length; k++) {
            if (board[k][j] >= '1' && board[k][j] <= '9' && !seenCharacter.add(board[k][j])) {
                return false;
            }
        }

        int dx = i/3 * 3;
        int dy = j/3 * 3;
        // check 3 * 3 block
        seenCharacter.clear();
        for (int k = dx; k < dx + 3; k++) {
            for (int l = dy; l < dy + 3; l++) {
                if (board[k][l] >= '1' && board[k][l] <= '9' && !seenCharacter.add(board[k][l])) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isValidSudoku(char[][] board) {
        Set<Character> seenCharacter;
        // check row
        for (int i = 0; i < board.length; i++) {
            seenCharacter = new HashSet<>();
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == '.' || board[i][j] < '1' || board[i][j] > '9' || !seenCharacter.add(board[i][j])) {
                    return false;
                }
            }
        }

        // check column
        for (int j = 0; j < board[0].length; j++) {
            seenCharacter = new HashSet<>();
            for (int i = 0; i < board.length; i++) {
                if (board[i][j] == '.' || board[i][j] < '1' || board[i][j] > '9' || !seenCharacter.add(board[i][j])) {
                    return false;
                }
            }
        }

        // check 3 * 3 block
        // check row
        for (int i = 0; i < board.length; i += 3) {
            seenCharacter = new HashSet<>();
            for (int j = 0; j < board[0].length; j += 3) {
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        if (board[k][l] == '.' || board[k][l] < '1' || board[k][l] > '9' || !seenCharacter.add(board[k][l])) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
