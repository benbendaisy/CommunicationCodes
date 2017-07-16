package com.example.lee.thirdRound;

import java.util.BitSet;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 7/14/17.
 */
public class SetMatrixZeroes {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        BitSet rows = new BitSet(matrix.length);
        BitSet columns = new BitSet(matrix[0].length);
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    rows.set(i);
                    columns.set(j);
                }
            }
        }

        // set row
        for (int i = 0; i < matrix.length; i++) {
            if (rows.get(i)) {
                for (int j = 0; j < matrix[0].length; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        // set column
        for (int j = 0; j < matrix[0].length; j++) {
            if (columns.get(j)) {
                for (int i = 0; i < matrix.length; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
