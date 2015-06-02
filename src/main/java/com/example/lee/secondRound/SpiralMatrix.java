package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 6/1/15.
 */
public class SpiralMatrix {
    //do it recursively
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == matrix || matrix.length < 1) return list;
        spiralOrder(matrix, 0, 0, list);
        return list;
    }

    public void spiralOrder(int[][] matrix, int rowDiff, int colDiff, List<Integer> list) {
        int row = matrix.length;
        int col = matrix[0].length;
        if (rowDiff > row - rowDiff - 1 || colDiff > col - colDiff - 1) return;
        for (int j = colDiff; j <= col - colDiff - 1; j++) list.add(matrix[rowDiff][j]);
        for (int i = rowDiff + 1; i <= row - rowDiff - 1; i++) list.add(matrix[i][col - colDiff -1]);
        if (row - rowDiff - 1 <= rowDiff || col - colDiff - 1 <= colDiff) return;
        for (int j = col - colDiff - 2; j >= colDiff; j--) list.add(matrix[row - rowDiff - 1][j]);
        for (int i = row - rowDiff - 2; i > rowDiff; i--) list.add(matrix[i][colDiff]);
        spiralOrder(matrix, rowDiff + 1, colDiff + 1, list);
    }


    //do it iteratively
    public List<Integer> spiralOrderI(int[][] matrix) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == matrix || matrix.length < 1) return list;
        int row = matrix.length;
        int col = matrix[0].length;
        int level = 0;
        while (level < row - level && level < col - level) {
            for (int j = level; j < col - level; j++) list.add(matrix[level][j]);
            if (level >= row - level - 1) break;
            for (int i = level + 1; i < row - level; i++) list.add(matrix[i][col - level - 1]);
            if (level >= col - level - 1) break;
            for (int j = col - level - 2; j >= level; j--) list.add(matrix[row - level - 1][j]);
            for (int i = row - level - 2; i > level; i--) list.add(matrix[i][level]);
            level++;
        }
        return list;
    }

    public static void main(String[] args) {
        int[][] matrix = {{2, 5, 8}, {4, 0, -1}};
        SpiralMatrix spiralMatrix = new SpiralMatrix();
        System.out.println(spiralMatrix.spiralOrder(matrix));
    }
}
