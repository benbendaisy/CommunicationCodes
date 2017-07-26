package com.example.lee.thirdRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 7/17/17.
 */
public class MaximalRectangle {
    /**
     * All three ways passed leetcode
     * O(n^3) solution
     * @param matrix
     * @return
     */
    public int maximalRectangleII(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int maxArea = 0;
        int[] height = new int[matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '0') {
                    height[j] = 0;
                } else {
                    height[j]++;
                }
            }
            maxArea = Math.max(maxArea, maxAreaInHist(height));
        }
        return maxArea;
    }
    private int maxAreaInHist(int[] height){
        if (height == null || height.length < 1) {
            return 0;
        }
        int len = height.length;
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        for (int i = 0; i < len; i++) {
            while (!stack.isEmpty() && height[stack.peek()] >= height[i]) {
                int t = stack.pop();
                maxArea = Math.max(maxArea, height[t] * (stack.isEmpty() ? i : i - stack.peek() - 1));
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            int t = stack.pop();
            maxArea = Math.max(maxArea, height[t] * (stack.isEmpty() ? len : len - stack.peek() - 1));
        }
        return maxArea;
    }

    /**
     * O(n^4) solution
     * @param matrix
     * @return
     */
    public int maximalRectangleI(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int maxArea = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '1') {
                    maxArea = Math.max(maxArea, calculateMaximalRectangle(matrix, i, j));
                }
            }
        }
        return maxArea;
    }

    private int calculateMaximalRectangle(char[][] matrix, int row, int col) {
        int maxArea = 0;
        int minWidth = Integer.MAX_VALUE;
        for (int i = row; i < matrix.length && matrix[i][col] == '1'; i++) {
            int width = 0;
            while (col + width < matrix[0].length && matrix[i][col + width] == '1') {
                width++;
            }
            if (width < minWidth) {
                minWidth = width;
            }
            maxArea = Math.max(maxArea, (i - row + 1) * minWidth);
        }
        return maxArea;
    }

    /**
     * O(n^2) solution
     * @param matrix
     * @return
     */
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int col = matrix[0].length;
        // current height of 1 in the metrics
        int[] height = new int[col];
        // current height can extend to left
        int[] l = new int[col];
        // current height can extend to right
        int[] r = new int[col];
        for (int j = 0; j < col; j++) {
            r[j] = col;
        }
        int maxArea = 0;
        for (int i = 0; i < matrix.length; i++) {
            int left = 0;
            int right = col;
            // calculate the height and how far that current height can extend
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    height[j]++;
                    l[j] = Math.max(l[j], left);
                } else {
                    left = j + 1;
                    height[j] = 0;
                    r[j] = col;
                    l[j] = 0;
                }
            }

            // calculate current height that can extend to right
            for (int j = col - 1; j >= 0; j--) {
                if (matrix[i][j] == '1') {
                    r[j] = Math.min(right, r[j]);
                    maxArea = Math.max(maxArea, (r[j] - l[j]) * height[j]);
                } else {
                    right = j;
                }
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        MaximalRectangle maximalRectangle = new MaximalRectangle();
        char[][] matrix = {{'0','1'}, {'1', 0}};
        System.out.println(maximalRectangle.maximalRectangle(matrix));
    }
}
