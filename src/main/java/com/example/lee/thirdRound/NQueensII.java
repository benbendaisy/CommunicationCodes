package com.example.lee.thirdRound;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created by benbendaisy on 7/9/17.
 */
public class NQueensII {
    public int totalNQueens(int n) {
        if (n < 1) {
            return 0;
        }
        AtomicInteger atomicInteger = new AtomicInteger(0);
        totalNQueensHelper(0, new int[n], atomicInteger);
        return atomicInteger.get();
    }

    private void totalNQueensHelper(int idx, int[] columns, AtomicInteger atomicInteger) {
        if (idx == columns.length) {
            atomicInteger.getAndIncrement();
            return;
        }
        for (int i = 0; i < columns.length; i++) {
            if (isValid(columns, idx, i)) {
                columns[idx] = i;
                totalNQueensHelper(idx + 1, columns, atomicInteger);
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
