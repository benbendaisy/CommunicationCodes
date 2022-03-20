package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/23/15.
 *
 * Follow up for "Unique Paths":
 *
 * Now consider if some obstacles are added to the grids. How many unique paths would there be?
 *
 * An obstacle and empty space is marked as 1 and 0 respectively in the grid.
 *
 * For example,
 * There is one obstacle in the middle of a 3x3 grid as illustrated below.
 *
 * [
 * [0,0,0],
 * [0,1,0],
 * [0,0,0]
 * ]
 * The total number of unique paths is 2.
 *
 * Note: m and n will be at most 100.
 */
public class UniquePathsII {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid == null){
            return 0;
        }

        int row = obstacleGrid.length;
        int col = obstacleGrid[0].length;
        int[][] dp = new int[row][col];
        if(obstacleGrid[0][0] == 1){
            dp[0][0] = 0;
        } else {
            dp[0][0] = 1;
        }
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(i >= 1 && j >= 1){
                    if(obstacleGrid[i][j] == 0){
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                    } else {
                        dp[i][j] = 0;
                    }
                } else if(i >= 1){
                    if(obstacleGrid[i][j] == 0){
                        dp[i][j] = dp[i - 1][j];
                    } else {
                        dp[i][j] = 0;
                    }
                } else if(j >= 1){
                    if(obstacleGrid[i][j] == 0){
                        dp[i][j] = dp[i][j - 1];
                    } else {
                        dp[i][j] = 0;
                    }
                }
            }
        }
        return dp[row - 1][col - 1];
    }
}
