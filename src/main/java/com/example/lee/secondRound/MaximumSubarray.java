package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/1/15.
 */
public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        if (null == nums || nums.length < 1) return 0;
        int max = Integer.MIN_VALUE, locMax = 0;
        for (int i : nums) {
            locMax += i;
            max = Math.max(max, locMax);
            if (locMax < 0) locMax = 0;
        }
        return max;
    }
}
