package com.example.lee.thirdRound;

public class Candy {
    public int candy(int[] ratings) {
        if (ratings == null || ratings.length == 0) {
            return 0;
        }
        int[] candies = new int[ratings.length];
        // from left to right
        candies[0] = 1;
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            } else {
                candies[i] = 1;
            }
        }
        int curMax = 1;
        int res = candies[ratings.length - 1];
        // from right to left
        for (int i = ratings.length - 2; i >= 0; i--) {
           if (ratings[i] > ratings[i + 1]) {
               curMax = curMax + 1;
           } else {
               curMax = 1;
           }
           res += Math.max(candies[i], curMax);
        }
        return res;
    }
}
