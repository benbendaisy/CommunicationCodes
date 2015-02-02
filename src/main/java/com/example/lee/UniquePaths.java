package com.example.lee;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 1/23/15.
 *
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
 *
 * The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
 *
 * How many possible unique paths are there?
 */
public class UniquePaths {

    //dynamic way
    public int uniquePaths(int m, int n) {
        if(m < 0 || n < 0){
            return 0;
        }

        int[][] dp = new int[m][n];
        dp[0][0] = 1;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(i >= 1 && j >= 1){
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                } else if(i >= 1){
                    dp[i][j] = dp[i - 1][j];
                } else if(j >= 1){
                    dp[i][j] = dp[i][j - 1];
                }
            }
        }

        return dp[m - 1][n - 1];
    }

    //recursive + memorization
    public int uniquePathsI(int m, int n) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        return uniquePaths(m, n, map);
    }

    public int uniquePaths(int m, int n, Map<String, Integer> map){
        if(m < 0 || n < 0){
            return 0;
        } else if(m == 0 && n == 0){
            return 1;
        } else if(map.containsKey(m + ":" + n)){
            return map.get(m + ":" + n);
        }

        int path = uniquePaths(m - 1, n) + uniquePaths(m, n - 1);
        map.put(m + ":" + n, path);
        return path;
    }
}
