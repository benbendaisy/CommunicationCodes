package com.example.lee.thirdRound;

public class BestTimeToBuyAndSellStockIII {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }
        int[] leftMax = new int[prices.length];
        int min = prices[0];
        for (int i = 1; i < prices.length; i++) {
            min = Math.min(min, prices[i]);
            leftMax[i] = Math.max(leftMax[i - 1], prices[i] - min);
        }
        int max = prices[prices.length - 1];
        int res = 0;
        for (int j = prices.length - 2; j >= 0; j--) {
            max = Math.max(max, prices[j]);
            res = Math.max(res, max - prices[j] + leftMax[j]);
        }
        return res;
    }
}
