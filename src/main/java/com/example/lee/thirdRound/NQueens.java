package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Created by benbendaisy on 7/9/17.
 */
public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        if (n < 1) {
            return Collections.emptyList();
        }
        int[] columns = new int[n];
        List<List<String>> res = new ArrayList<>();
        solveNQueens(0, columns, res);
        return res;
    }

    private void solveNQueens(int idx, int[] columns, List<List<String>> res) {
        if (idx == columns.length) {
            char[][] boards = new char[columns.length][columns.length];
            for (int i = 0; i < columns.length; i++) {
                Arrays.fill(boards[i], '.');
            }
            List<String> list = new ArrayList<>();
            for (int i = 0; i < columns.length; i++) {
                boards[i][columns[i]] = 'Q';
                list.add(new String(boards[i]));
            }
            res.add(list);
            return;
        }
        for (int j = 0; j < columns.length; j++) {
            if (isValid(columns, idx, j)) {
                columns[idx] = j;
                solveNQueens(idx + 1, columns, res);
            }
        }
    }
    private boolean isValid(int[] columns, int row, int column) {
        for (int i = 0; i < row; i++) {
            if (columns[i] == column || Math.abs(i - row) == Math.abs(columns[i] - column)) {
                return false;
            }
        }
        return true;
    }
}
