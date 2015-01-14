package com.example.lee;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Given a 2D board and a word, find if the word exists in the grid.
 *
 * The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
 *
 * For example,
 * Given board =
**
 * [
 * ["ABCE"],
 * ["SFCS"],
 * ["ADEE"]
 * ]
 * word = "ABCCED", -> returns true,
 * word = "SEE", -> returns true,
 * word = "ABCB", -> returns false.
 */
public class WordSearch {
    public boolean exist(char[][] board, String word) {
        if(board == null || word == null) {
            return false;
        } else if(word.length() == 0){
            return true;
        }
        for(int i = 0; i < word.length(); i++){
            for(int j = 0; j < word.length(); j++){
                if(board[i][j] == word.charAt(0)){
                    if(existHelper(board, word, i, j)){
                        return true;
                    }
                }
            }
        }
    }
    private boolean existHelper(char[][] board, String word, int row, int col){
        if(row >= board.length || row < 0 || col >= board[0].length || col < 0){
            return false;
        } else if(word.length() == 0){
            return true;
        }

        boolean result = false;
        //up
        if(row - 1 >= 0 && board[row - 1][col] == word.charAt(0)){
            result = existHelper(board, word.substring(1), row - 1, col);
        }
        if(result){
            return true;
        }

        //right
        if(col + 1 < board[0].length && board[row][col + 1] == word.charAt(0)){
            result = existHelper(board, word.substring(1), row, col + 1);
        }
        if(result){
            return true;
        }

        //down
        if(row + 1 < board.length && board[row + 1][col] == word.charAt(0)){
            result = existHelper(board, word.substring(1), row + 1, col);
        }
        if(result){
            return true;
        }

        //left
        if(col - 1 >= 0 && board[row][col - 1] == word.charAt(0)){
            result = existHelper(board, word.substring(1), row, col - 1);
        }

        if(result){
            return true;
        }

        return false;
    }
}
