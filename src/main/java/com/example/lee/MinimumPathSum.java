package com.example.lee;

/**
 * Created by benbendaisy on 1/19/15.
 * Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
 *
 * Note: You can only move either down or right at any point in time.
 */
public class MinimumPathSum {
    public int minPathSum(int[][] grid) {
        if(grid == null){
            return 0;
        }
        int row = grid.length;
        int col = grid[0].length;
        int[][] dp = new int[row][col];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < row; i++) {
            dp[i][0] = grid[i][0] + dp[i - 1][0];
        }
        for (int j = 1; j < col; j++) {
            dp[0][j] = grid[0][j] + dp[0][j - 1];
        }
        for (int i = 1; i < row; i++){
            for (int j = 1; j < col; j++){
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[row - 1][col - 1];
    }

    public int minPathSumI(int[][] grid) {
        if(grid == null){
            return 0;
        }
        int row = grid.length;
        int col = grid[0].length;
        int[][] dp = new int[row + 1][col + 1];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < row; i++) {
            dp[i][0] = grid[i][0] + dp[i - 1][0];
        }
        for (int j = 1; j < col; j++) {
            dp[0][j] = grid[0][j] + dp[0][j - 1];
        }
        for (int i = 1; i <= row; i++){
            for (int j = 1; j <= col; j++){
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i - 1][j - 1];
            }
        }
        return dp[row][col];
    }

    public static void main(String[] args) {
        MinimumPathSum minimumPathSum = new MinimumPathSum();
        int[][] array = {{1}};
        System.out.println(minimumPathSum.minPathSumI(array));
    }
}
