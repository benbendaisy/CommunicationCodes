package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/11/17.
 */
public class UniquePathsII {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0].length == 0) {
            return 0;
        }
        int[][] dp = new int[obstacleGrid.length][obstacleGrid[0].length];
        dp[0][0] = obstacleGrid[0][0] == 1 ? 0 : 1;

        for (int i = 1; i < obstacleGrid.length; i++) {
            dp[i][0] = obstacleGrid[i][0] == 0 ? dp[i - 1][0] : 0;
        }

        for (int j = 1; j < obstacleGrid[0].length; j++) {
            dp[0][j] = obstacleGrid[0][j] == 0 ? dp[0][j - 1] : 0;
        }

        for (int i = 1; i < obstacleGrid.length; i++) {
            for (int j = 1; j < obstacleGrid[0].length; j++) {
                int top = obstacleGrid[i - 1][j] == 0 ? dp[i - 1][j] : 0;
                int left = obstacleGrid[i][j - 1] == 0 ? dp[i][j - 1] : 0;
                dp[i][j] = obstacleGrid[i][j] == 0 ? top + left : 0;
            }
        }
        return dp[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
    }
}
