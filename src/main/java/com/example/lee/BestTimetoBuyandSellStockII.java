package com.example.lee;

/**
 * Created by benbendaisy on 12/30/14.
 * Say you have an array for which the ith element is the price of a given stock on day i.
 * Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
 *
 * there are two possible options:
 * 1, each time, buy the stock at the lowest price and sell the price before it decrease
 * 2, always sell the stock if there is any gains
 */

public class BestTimetoBuyandSellStockII {
    //option 1
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length < 2){
            return 0;
        }
        int min = prices[0], total = 0;
        for(int i = 1; i < prices.length; i++){
            if(prices[i] < prices[i-1]){
                int delta = prices[i-1] - min;
                if(delta > 0){
                    total += delta;
                }
                min = prices[i];
            }
        }
        if(prices[prices.length - 1] > min){
            total += prices[prices.length - 1] - min;
        }
        return total;
    }

    //option 2
    public int maxProfitI(int[] prices) {
        if(prices == null || prices.length < 2){
            return 0;
        }
        int min = prices[0], total = 0;
        for(int i = 1; i < prices.length; i++){
            int delta = prices[i] - prices[i-1];
            if(delta > 0){
                total += delta;
            }
        }
        return total;
    }
}
