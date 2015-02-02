package com.example.lee.model;

/**
 * Created by benbendaisy on 2/1/15.
 *
 * You are given an n x n 2D matrix representing an image.
 *
 * Rotate the image by 90 degrees (clockwise).
 *
 * move each
 * Follow up:
 * Could you do this in-place?
 */

public class RotateImage {
    public void rotate(int[][] matrix) {
        if(matrix == null){
            return;
        }
        int row = matrix.length;
        int column = matrix[0].length;
        if(row != column){
            return;
        }
        int n = row / 2;
        //int[] t = new int[row];
        for(int i = 0; i < n; i++){
            for(int j = i; j < row - i - 1; j++){
                //save right column
                int t = matrix[j][row - i - 1];
                matrix[j][row - i - 1] = matrix[i][j];
                //save bottom column
                int t1 = matrix[row - i - 1][row - j - 1];
                matrix[row - i - 1][row - j - 1] = t;
                //save left column
                t = matrix[row - j - 1][i];
                matrix[row - j - 1][i] = t1;
                matrix[i][j] = t;
            }
        }
    }

    public static void main(String[] args) {
        RotateImage rotateImage = new RotateImage();
        int[][] image = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        rotateImage.rotate(image);
        System.out.println(image);
    }
}
