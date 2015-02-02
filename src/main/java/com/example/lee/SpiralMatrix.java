package com.example.lee;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/27/15.
 *
 * Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 *
 * For example,
 * Given the following matrix:
 *
 * [
 * [ 1, 2, 3 ],
 * [ 4, 5, 6 ],
 * [ 7, 8, 9 ]
 * ]
 * You should return [1,2,3,6,9,8,7,4,5].
 */
public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list = new ArrayList<Integer>();
        if(matrix == null || matrix.length == 0){
            return list;
        }
        int row = matrix.length;
        int col = matrix[0].length;
        int level = 0;
        int mid = row / 2;
        while(level < row - level && level < col - level){
            //the upper row
            for(int j = level; j < col - level; j++){
                list.add(matrix[level][j]);
            }


            //the right col
            for(int i = level + 1; i < row - level; i++){
                list.add(matrix[i][col - level - 1]);
            }

            if(row - level - 1 <= level){
                break;
            }
            //the bottom row
            for(int j = col - level - 2; j > level; j--){
                list.add(matrix[row - level - 1][j]);
            }

            if(col - level - 1 <= level){
                break;
            }
            //the left col
            for(int i = row - level - 1; i > level; i--){
                list.add(matrix[i][level]);
            }

            level++;
        }
        return list;
    }

    public static void main(String[] args) {
        SpiralMatrix spiralMatrix = new SpiralMatrix();
        int[][] A = {{1, 2}, {3, 4}};
        System.out.println(spiralMatrix.spiralOrder(A));
    }
}
