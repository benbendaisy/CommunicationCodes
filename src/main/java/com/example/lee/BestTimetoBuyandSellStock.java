package com.example.lee;

/**
 * Created by benbendaisy on 12/30/14.
 * Say you have an array for which the ith element is the price of a given stock on day i.
 * If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
 */
public class BestTimetoBuyandSellStock {
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length < 2){
            return 0;
        }

        int len = prices.length;
        int min = Integer.MAX_VALUE, max = 0;
        for(int i = 0; i < len; i++){
            int localMax = prices[i] - min;
            if( localMax > max){
                max = localMax;
            }
            if(prices[i] < min){
                min = prices[i];
            }
        }

        return max;
    }
}
