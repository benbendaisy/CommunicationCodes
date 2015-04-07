package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/4/15.
 */
public class Candy {
    public int candy(int[] ratings) {
        if (null == ratings) {
            return 0;
        } else if (ratings.length < 2) {
            return 1;
        }

        int[] l = new int[ratings.length];
        int[] r = new int[ratings.length];
        l[0] = 1;
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                l[i] = l[i - 1] + 1;
            } else {
                l[i] = 1;
            }
        }
        r[ratings.length - 1] = 1;
        for (int i = ratings.length - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                r[i] = r[i + 1] + 1;
            } else {
                r[i] = 1;
            }
        }
        int cnt = 0;
        for (int i = 0; i < ratings.length; i++) {
            cnt += l[i] > r[i] ? l[i] : r[i];
        }
        return cnt;
    }
}
