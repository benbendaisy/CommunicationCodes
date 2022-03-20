package com.example.lee.secondRound;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 6/22/15.
 */
public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        if (board == null || board.length != 9 || board[0].length != 9) {
            return false;
        }

        //check row
        Set<Character> seenCharacter;
        for (int i = 0; i < board.length; i++) {
            seenCharacter = new HashSet<>();
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] != '.' && (board[i][j] < '1' || board[i][j] > '9' || !seenCharacter.add(board[i][j]))) {
                    return false;
                }
            }
        }

        //check column
        for (int j = 0; j < board[0].length; j++) {
            seenCharacter = new HashSet<>();
            for (int i = 0; i < board.length; i++) {
                if (board[i][j] != '.' && (board[i][j] < '1' || board[i][j] > '9' || !seenCharacter.add(board[i][j]))) {
                    return false;
                }
            }
        }

        //check 3 * 3 block
        for (int i = 0; i < board.length; i += 3) {
            for (int j = 0; j < board[0].length; j += 3) {
                seenCharacter = new HashSet<>();
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        if (board[k][l] != '.' && (board[k][l] < '1' || board[k][l] > '9' || !seenCharacter.add(board[k][l]))) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
