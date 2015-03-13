package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/14/15.
 *
 * Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
 *
 * Integers in each row are sorted from left to right.
 * The first integer of each row is greater than the last integer of the previous row.
 * For example,
 *
 * Consider the following matrix:
 *
 * [
 * [1,   3,  5,  7],
 * [10, 11, 16, 20],
 * [23, 30, 34, 50]
 * ]
 * Given target = 3, return true.
 */
public class Searcha2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null){
            return false;
        }
        int left = 0, right = matrix[0].length - 1;
        while(left < matrix.length && right >= 0){
            if(matrix[left][right] == target){
                return true;
            }else if(matrix[left][right] < target){
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
}
