package com.example.lee.thirdRound;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 7/5/17.
 */
public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        if (board == null || board.length != 9 || board[0].length != 9) {
            return false;
        }

        Set<Character> seenCharacter;
        // check row
        for (int i = 0; i < board.length; i++) {
            seenCharacter = new HashSet<>();
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] != '.' && (board[i][j] < '1' || board[i][j] > '9' || !seenCharacter.add(board[i][j]))) {
                    return false;
                }
            }
        }

        // check column
        for (int j = 0; j < board[0].length; j++) {
            seenCharacter = new HashSet<>();
            for (int i = 0; i < board.length; i++) {
                if (board[i][j] != '.' && (board[i][j] < '1' || board[i][j] > '9' || !seenCharacter.add(board[i][j]))) {
                    return false;
                }
            }
        }

        // check 3 * 3 block
        for (int i = 0; i < board.length; i += 3) {
            for (int j = 0; j < board[0].length; j += 3) {
                seenCharacter = new HashSet<>();
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        int idx = k + i;
                        int idy = l + j;
                        if (board[idx][idy] != '.' && (board[idx][idy] < '1' || board[idx][idy] > '9' || !seenCharacter.add(board[idx][idy]))) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }


    public static void main(String[] args) {
        ValidSudoku validSudoku = new ValidSudoku();
        char[][] board = new char[][]{
                {'.','8','7','6','5','4','3','2','1'},
                {'2','.','.','.','.','.','.','.','.'},
                {'3','.','.','.','.','.','.','.','.'},
                {'4','.','.','.','.','.','.','.','.'},
                {'5','.','.','.','.','.','.','.','.'},
                {'6','.','.','.','.','.','.','.','.'},
                {'7','.','.','.','.','.','.','.','.'},
                {'8','.','.','.','.','.','.','.','.'},
                {'9','.','.','.','.','.','.','.','.'},
        };
        System.out.println(validSudoku.isValidSudoku(board));
    }

}
