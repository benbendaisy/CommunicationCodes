package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/8/15.
 *
 * Say you have an array for which the ith element is the price of a given stock on day i.
 *
 * If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
 */
public class BestTimetoBuyandSellStock {
    public int maxProfit(int[] prices) {
        if (null == prices || prices.length < 1) return 0;
        int max = 0, min = prices[0];
        for (int i = 0; i < prices.length; i++) {
            min = Math.min(min, prices[i]);
            max = Math.max(max, prices[i] - min);
        }
        return max;
    }
}
