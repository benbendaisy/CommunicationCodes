package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 3/17/15.
 */
public class MaximumGap {
    public int maximumGap(int[] num) {
        if (null == num || num.length < 2) {
            return 0;
        }
        int len = num.length;
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int i = 0; i < len; i++) {
            min = Math.min(min, num[i]);
            max = Math.max(max, num[i]);
        }
        int bucket = (int) Math.ceil((double) (max - min) / (len - 1));
        int[] bSortMin = new int[len];
        int[] bSortMax = new int[len];
        for (int i = 0; i < len; i++) {
            bSortMin[i] = Integer.MAX_VALUE;
            bSortMax[i] = Integer.MIN_VALUE;
        }
        for (int i = 0; i < len; i++) {
            int idx = (num[i] - min) / bucket;
            bSortMin[idx] = Math.min(bSortMin[idx], num[i]);
            bSortMax[idx] = Math.max(bSortMax[idx], num[i]);
        }
        int maxGap = 0, previous = min;
        for (int i = 0; i < len; i++) {
            if (bSortMin[i] == Integer.MAX_VALUE || bSortMax[i] == Integer.MIN_VALUE) {
                continue;
            }
            maxGap = Math.max(maxGap, bSortMin[i] - previous);
            previous = bSortMax[i];
        }
        return maxGap;
        //inner max elements

    }
}
