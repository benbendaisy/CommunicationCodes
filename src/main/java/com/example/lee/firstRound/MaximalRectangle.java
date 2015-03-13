package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
 */
public class MaximalRectangle {
    /*
     * http://hi.baidu.com/mzry1992/item/030f9740e0475ef7dc0f6cba
     * http://www.mitbbs.com/article_t/JobHunting/32294463.html
     */
    public int maximalRectangle(char[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return 0;
        }
        int rows = matrix.length;
        int columns = matrix[0].length;

        //current height
        int[] height = new int[columns];
        //left index that current height can extend
        int[] l = new int[columns];
        //right index that current height can extend
        int[] r = new int[columns];

        //initial right index to right column
        for(int i = 0; i < columns; i++){
            r[i] = columns;
        }
        int max = 0;
        for(int i = 0; i < rows; i++){
            int left = 0;
            int right = columns;
            for(int j = 0; j < columns; j++){
                if(matrix[i][j] == '1'){
                    height[j]++;
                    l[j] = Math.max(left, l[j]);
                } else {
                    height[j] = 0;
                    l[j] = 0;
                    left = j + 1;
                    r[j] = columns;
                }
            }

            for(int j = columns - 1; j >= 0; j--){
                if(matrix[i][j] == '1'){
                    r[j] = Math.min(right, r[j]);
                    max = Math.max(max, (r[j] - l[j]) * height[j]);
                } else {
                    right = j;
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        MaximalRectangle maximalRectangle = new MaximalRectangle();
        char[][] matrix = {{'0','1'}, {'1', 0}};
        System.out.println(maximalRectangle.maximalRectangle(matrix));
    }
}
