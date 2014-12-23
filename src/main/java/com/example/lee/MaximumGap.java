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
