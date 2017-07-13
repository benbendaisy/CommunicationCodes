package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by benbendaisy on 7/9/17.
 */
public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix == null || matrix.length < 1) {
            return Collections.emptyList();
        }
        List<Integer> list = new ArrayList<>();
        int row = matrix.length;
        int column = matrix[0].length;
        double minIteration = Math.min(Math.ceil((double) row / 2.0), Math.ceil((double) column / 2.0));
        for (int i = 0; i < minIteration; i++) {
            // top row
            for (int j = i; j < column - i; j++) {
                list.add(matrix[i][j]);
            }

            // single row
            if ( i >= row - i - 1) {
                break;
            }


            // right column
            for (int j = i + 1; j < row - i; j++) {
                list.add(matrix[j][column - i - 1]);
            }

            // bottom row
            for (int j = column - i - 2; j >= i; j--) {
                list.add(matrix[row - i - 1][j]);
            }

            // single column
            if (i >= column - i -1) {
                break;
            }
            // left column
            for (int j = row - i - 2; j > i; j--) {
                list.add(matrix[j][i]);
            }
        }
        return list;
    }

    public static void main(String[] args) {
//        int[][] metrics = {{2,3}};
        int[][] metrics = {{1,11},{2,12},{3,13},{4,14},{5,15},{6,16},{7,17},{8,18},{9,19},{10,20}};
        SpiralMatrix spiralMatrix = new SpiralMatrix();
        System.out.println(spiralMatrix.spiralOrder(metrics));
    }
}
