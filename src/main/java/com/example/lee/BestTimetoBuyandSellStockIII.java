package com.example.lee;

/**
 * Created by benbendaisy on 12/30/14.
 * Say you have an array for which the ith element is the price of a given stock on day i.
 * Design an algorithm to find the maximum profit. You may complete at most two transactions.
 * Note:
 * You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
 * refer to: http://blog.csdn.net/fightforyourdream/article/details/14503469
 * basic idea is find an index that split price array into two arrays and find max profit in both sides
 */
public class BestTimetoBuyandSellStockIII {
    //o(n) solution
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length < 2){
            return 0;
        }

        int len = prices.length;
        int[] left = new int[len];
        int[] right = new int[len];

        int min = prices[0];
        for(int i = 1; i < len; i++){
            min = Math.min(min, prices[i]);
            left[i] = Math.max(left[i-1], prices[i] - min);
        }
        int max = prices[len - 1];
        for(int i = len - 2; i >= 0; i--){
            max = Math.max(max, prices[i]);
            right[i] = Math.max(right[i+1], max - prices[i]);
        }

        max = 0;
        for(int i = 0; i < len; i++){
            max = Math.max(max, left[i] + right[i]);
        }

        return max;
    }

    //time complexity o(n^2). can not pass big data test
    public int maxProfitI(int[] prices){
        if(prices == null || prices.length < 2){
            return 0;
        }
        BestTimetoBuyandSellStock bestTimetoBuyandSellStock = new BestTimetoBuyandSellStock();
        int max = 0;
        for(int i = 0; i < prices.length; i++){
            int leftMax = maxProfitHelper(prices, 0, i);
            int rightMax = maxProfitHelper(prices, i, prices.length);
            max = Math.max(max, leftMax + rightMax);
        }
        return  max;
    }

    public int maxProfitHelper(int[] prices, int start, int end) {
        int min = Integer.MAX_VALUE, max = 0;
        for(int i = start; i < end; i++){
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
