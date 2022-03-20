package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/8/15.
 * Say you have an array for which the ith element is the price of a given stock on day i.
 *
 * Design an algorithm to find the maximum profit. You may complete at most two transactions.
 *
 * Note:
 * You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
 */
public class BestTimetoBuyandSellStockIII {
    public int maxProfit(int[] prices) {
        int k = 2;
        if (null == prices || prices.length < 2 || k < 1) {
            return 0;
        }
        int[][] dp = new int[prices.length + 1][k + 1];
        for (int j = 1; j <= k; j++) {
            int t = dp[0][j - 1] - prices[0];
            for (int i = 1; i <= prices.length; i++) {
                dp[i][j] = Math.max(dp[i - 1][j], t + prices[i - 1]);
                if (i < prices.length) t = Math.max(t, dp[i][j - 1] - prices[i]);
            }
        }
        return dp[prices.length][k];
    }

    public int maxProfitI(int[] prices) {
        if (null == prices || prices.length < 2) {
            return 0;
        }
        int[] l = new int[prices.length];
        int min = prices[0], max = 0;
        for (int i = 0; i < prices.length; i++) {
            min = Math.min(min, prices[i]);
            max = Math.max(max, prices[i] - min);
            l[i] = max;
        }
        max = prices[prices.length - 1];
        int lMax = 0;
        int tMax = 0;
        for (int i = prices.length - 1; i >= 0; i--) {
            max = Math.max(max, prices[i]);
            lMax = Math.max(lMax, max - prices[i]);
            tMax = Math.max(tMax, lMax + l[i]);
        }
        return tMax;
    }
}
