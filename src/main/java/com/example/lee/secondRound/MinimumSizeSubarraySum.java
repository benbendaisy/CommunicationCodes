package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/11/15.
 *
 * Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
 *
 * For example, given the array [2,3,1,2,4,3] and s = 7,
 * the subarray [4,3] has the minimal length under the problem constraint.
 */
public class MinimumSizeSubarraySum {
    public int minSubArrayLen(int s, int[] nums) {
        if (null == nums) return 0;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum >= s) {
                    min = Math.min(min, j - i + 1);
                    break;
                }
            }

        }
        return min == Integer.MAX_VALUE ? 0 : min;
    }

    public static void main(String[] args) {
        MinimumSizeSubarraySum mss = new MinimumSizeSubarraySum();
        int[] arrs = {10,5,13,4,8,4,5,11,14,9,16,10,20,8};
        System.out.println(mss.minSubArrayLen(80, arrs));
    }
}
