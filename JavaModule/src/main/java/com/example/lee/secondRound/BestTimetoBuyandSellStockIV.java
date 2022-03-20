package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/8/15.
 * Say you have an array for which the ith element is the price of a given stock on day i.
 *
 * Design an algorithm to find the maximum profit. You may complete at most k transactions.
 *
 * Note:
 * You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
 */
public class BestTimetoBuyandSellStockIV {
    public int maxProfit(int k, int[] prices) {
        if (k < 1 || prices.length < 1) return 0;
        if (prices.length <= k) return maxProfit(prices);
        //dp represents the max that j transactions in i days
        int[][] dp = new int[prices.length + 1][k + 1];
        for (int j = 1; j <= k; j++) {
            //t represent j - 1 transactions minus the price that stock is bought
            int t = dp[0][j - 1] - prices[0];
            for (int i = 1; i <= prices.length; i++) {
                //the max that j tractions in i days equals to the max of either the max
                // that j tractions in i - 1 days or j - 1 transactions plus the max
                // that happens in this round
                dp[i][j] = Math.max(dp[i - 1][j], t + prices[i - 1]);
                //update the temp max that happens in this round
                if (i < prices.length) t = Math.max(t, dp[i][j - 1] - prices[i]);
            }
        }
        return dp[prices.length][k];
    }

    private int maxProfit(int[] prices) {
        int total = 0;
        for (int i = 1; i < prices.length; i++) {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) {
                total += diff;
            }
        }
        return total;
    }
}
