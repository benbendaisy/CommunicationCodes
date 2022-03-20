package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/8/15.
 *
 * Say you have an array for which the ith element is the price of a given stock on day i.
 *
 * Design an algorithm to find the maximum profit. You may complete at most k transactions.
 *
 * Note:
 * You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
 */

public class BestTimetoBuyandSellStockIV {

    //refer to http://blog.csdn.net/foreverling/article/details/43911309 for more detail
    public int maxProfit(int k, int[] prices) {
        if (null == prices || prices.length < 2 || k < 1) {
            return 0;
        }
        //handle the situation when k is far bigger than the length of array
        if (prices.length < k) {
            return maxProfit(prices);
        }

        //local is used to store local revenue that took j trasactions in i days and
        //sold the stock in the i day
        int[][] local = new int[prices.length][k + 1];
        //the best revenue that took j trasactions in i days
        int[][] global = new int[prices.length][k + 1];
        for (int i = 1; i < prices.length; i++) {
            int diff = prices[i] - prices[i - 1];
            for (int j = 1; j <= k; j++) {
                local[i][j] = Math.max(global[i - 1][j - 1] + Math.max(diff, 0), local[i - 1][j] + diff);
                global[i][j] = Math.max(global[i - 1][j], local[i][j]);
            }
        }
        return global[prices.length - 1][k];
    }

    //refer to http://blog.csdn.net/linhuanmars/article/details/23236995
    public int maxProfitI(int k, int[] prices) {
        if (null == prices || prices.length < 2 || k < 1) {
            return 0;
        }
        if (prices.length < k) {
            return maxProfit(prices);
        }

        //refer to local best revenue that sold the stock at ith day
        int[] local = new int[k + 1];
        //refer to global best revenue
        int[] global = new int[k + 1];
        for (int i = 0; i < prices.length - 1; i++) {
            int diff = prices[i + 1] - prices[i];
            for (int j = k; j > 0; j--) {
                local[j] = Math.max(global[j - 1] + Math.max(diff, 0), local[j] + diff);
                global[j] = Math.max(global[j], local[j]);
            }
        }
        return global[k];
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

    public int maxProfitII(int k, int[] prices) {
        if (null == prices || prices.length < 2|| k < 1) {
            return 0;
        }
        int[] left = new int[prices.length];
        int[] right = new int[prices.length];
        int idx = 1, min = prices[idx];
        left[0] = 0;
        while (idx < prices.length) {
            min = Math.min(min, prices[idx]);
            left[idx] = Math.max(left[idx - 1], prices[idx] - min);
            idx++;
        }

        idx = prices.length - 1;
        int max = prices[idx];
        right[0] = 0;
        while (idx < prices.length) {
            max = Math.max(max, prices[idx]);
            right[idx] = Math.max(right[idx + 1], max - prices[idx]);
            idx--;
        }
        return 0;
    }

    public static void main(String[] args) {
        int[] prices = {106, 373, 495, 46, 359, 919, 906, 440, 783, 583, 784, 73, 238, 701, 972, 308, 165, 774, 990,
                675, 737, 990, 713, 157, 211, 880, 961, 132, 980, 136, 285, 239, 628, 221, 948, 939, 28, 541, 414, 180,
                171, 640, 297, 873, 59, 814, 832, 611, 868, 633, 101, 67, 396, 264, 445, 548, 257, 656, 624, 71, 607, 67,
                836, 14, 373, 205, 434, 203, 661, 793, 45, 623, 140, 67, 177, 885, 155, 764, 363, 269, 599, 32, 228, 111,
                102, 565, 918, 592, 604, 244, 982, 533, 781, 604, 115, 429, 33, 894, 778, 885, 145, 888, 577, 275, 644,
                824, 277, 302, 182, 94, 479, 563, 52, 771, 544, 794, 964, 827, 744, 366, 548, 761, 477, 434, 999, 86,
                1000, 5, 99, 311, 346, 609, 778, 937, 372, 793, 754, 191, 592, 860, 748, 297, 610, 386, 146, 220, 7, 113,
                657, 438, 482, 700, 158, 884, 877, 964, 777, 139, 809, 489, 383, 92, 581, 970, 899, 947, 864, 443, 490,
                825, 674, 906, 402, 270, 416, 611, 949, 476, 775, 899, 837, 796, 227, 232, 226, 11, 266, 889, 215, 6, 182,
                430, 5, 706, 994, 128, 359, 841, 439, 263, 491, 689, 638, 485, 763, 695, 135, 800, 763, 54, 569, 387, 112
        };
        BestTimetoBuyandSellStockIV bestTimetoBuyandSellStock = new BestTimetoBuyandSellStockIV();
        System.out.println(bestTimetoBuyandSellStock.maxProfit(1000000000, prices));
    }
}
