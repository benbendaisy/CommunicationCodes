package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 1/27/15.
 *
 * The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
 * Given an integer n, return all distinct solutions to the n-queens puzzle.
 *
 * Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
 *
 * For example,
 * There exist two distinct solutions to the 4-queens puzzle:
 *
 * [
 * [".Q..",  // Solution 1
 * "...Q",
 * "Q...",
 * "..Q."],
 *
 * ["..Q.",  // Solution 2
 * "Q...",
 * "...Q",
 * ".Q.."]
 * ]
 */
public class NQueens {
    public List<String[]> solveNQueens(int n) {
        List<String[]> list = new ArrayList<String[]>();
        if(n <= 0){
            return list;
        }
        int[] columns = new int[n];
        solveNQueens(n, 0, columns, list);
        return list;
    }

    public void solveNQueens(int n, int row, int[] columns, List<String[]> list){
        if(row == n){
            char[] chs = new char[n];
            for(int j = 0; j < n; j++){
                chs[j] = '.';
            }
            String[] strs = new String[n];
            for(int i = 0; i < n; i++){
                chs[columns[i]] = 'Q';
                strs[i] = new String(chs);
                chs[columns[i]] = '.';
            }
            list.add(strs);
            return;
        }

        //place queen for the row
        for(int i = 0; i < n; i++){
            if(canPlaceQueen(columns, i, row)){
                columns[row] = i;
                solveNQueens(n, row + 1, columns, list);
            }
        }
    }

    private boolean canPlaceQueen(int[] columns, int column, int row){
        for(int i = 0; i < row; i++){
            if(columns[i] == column || Math.abs(i - row) == Math.abs(columns[i] - column)){
                return false;
            }
        }
        return true;
    }
}
