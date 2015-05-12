package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/11/15.
 */
public class ClimbingStairs {
    public int climbStairs(int n) {
        if (n < 1) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 2] + dp[i - 1];
        }
        return dp[n];
    }

    public int climbStairsI(int n) {
        if (n < 1) return 0;
        if (n == 1) return 1;
        int pre1 = 1;
        if (n == 2) return 2;
        int pre2 = 2;
        int cur = 0;
        for (int i = 3; i <= n; i++) {
            cur = pre1 + pre2;
            pre1 = pre2;
            pre2 = cur;
        }
        return cur;
    }

}
