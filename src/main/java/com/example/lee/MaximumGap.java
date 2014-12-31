package com.example.lee;

/**
 * Created by benbendaisy on 12/15/14.
 * Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
 * Try to solve it in linear time/space.
 * Return 0 if the array contains less than 2 elements.
 * You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
 */
public class MaximumGap {
    public int maximumGap(int[] num) {
        if(num == null || num.length < 2){
            return 0;
        }
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for(int e : num){
            if(e < min){
                min = e;
            }
            if(e > max){
                max = e;
            }
        }

        //find bucket size
        int len = num.length;
        int gap = (int) Math.ceil(((double)(max - min))/(len - 1));;
        int[] gapMin = new int[len];
        int[] gapMax = new int[len];

        for(int i = 0; i < len; i++){
            gapMin[i] = Integer.MAX_VALUE;
            gapMax[i] = Integer.MIN_VALUE;
        }

        //put element into buckets
        for(int e : num){
            int index = (e - min) / gap;
            gapMin[index] = Math.min(gapMin[index], e);
            gapMax[index] = Math.max(gapMax[index], e);
        }

        int maxGap = 0;

        //find max gap between buckets
        int previous = min;
        for(int i = 0; i < len; i++){
            if (gapMin[i] == Integer.MAX_VALUE && gapMax[i] == Integer.MIN_VALUE){
                // empty bucket
                continue;
            }
            maxGap = Math.max(maxGap, gapMin[i] - previous);
            previous = gapMax[i];
        }

        return maxGap;
    }
    public int maximumGapI(int[] num) {
        if(num == null || num.length <= 2){
            return 0;
        }
        int max = Integer.MIN_VALUE;
        for(int i = 1; i < num.length; i++){
            int locMax = Math.abs(num[i] - num[i-1]);
            if(locMax > max){
                max = locMax;
            }
        }
        return max;
    }
}
