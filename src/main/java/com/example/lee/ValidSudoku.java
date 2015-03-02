package com.example.lee;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 2/6/15.
 *
 * Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
 *
 * The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
 *
 *
 * A partially filled sudoku which is valid.
 *
 *
 */
public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        if(board == null || board.length != 9 || board[0].length != 9){
            return false;
        }

        return isValid(board);
    }

    private boolean isValid(char[][] board){
        int row = board.length;
        int col = board[0].length;
        //check row
        for(int i = 0; i < row; i++){
            Set<Integer> set = new HashSet<Integer>();
            for(int j = 0; j < col; j++){
                if(board[i][j] != '.'){
                    if(board[i][j] >= '1' && board[i][j] <= '9'){
                        if(!set.add(board[i][j] - '0')){
                            return false;
                        }
                    } else {
                        return false;
                    }
                }
            }
        }

        //check column
        for(int j = 0; j < col; j++){
            Set<Integer> set = new HashSet<Integer>();
            for(int i = 0; i < row; i++){
                if(board[i][j] != '.'){
                    if(board[i][j] >= '1' && board[i][j] <= '9'){
                        if(!set.add(board[i][j] - '0')){
                            return false;
                        }
                    } else {
                        return false;
                    }
                }
            }
        }

        //check submatrix
        for(int i = 0; i < row; i = i + 3){
            Set<Integer> set = new HashSet<Integer>();
            for(int j = 0; j < col; j = j + 3){
                if(board[i][j] != '.'){
                    if(board[i][j] >= '1' && board[i][j] <= '9'){
                        if(!set.add(board[i][j] - '0')){
                            return false;
                        }
                    } else {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    private boolean isValid(char[][] board, int rowIdx, int colIdx){
        for(int i = rowIdx; i < rowIdx + 3; i++){
            Set<Integer> set = new HashSet<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));
            for(int j = colIdx; j < colIdx + 3; j++){
                if(board[i][j] != '.'){
                    if(!set.contains(board[i][j])){
                        return false;
                    } else {
                        set.remove(board[i][j]);
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char[][] matrix = {{'.','8','7','6','5','4','3', '2', '1'},
                {'2', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'3', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'4', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'5', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'6', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'7', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'8', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'9', '.', '.', '.', '.', '.', '.', '.', '.'}
        };
        ValidSudoku validSudoku = new ValidSudoku();
        System.out.println(validSudoku.isValidSudoku(matrix));
    }
}
