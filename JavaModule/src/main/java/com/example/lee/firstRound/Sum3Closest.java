package com.example.lee.firstRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 3/3/15.
 *
 * Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
 *
 * For example, given array S = {-1 2 1 -4}, and target = 1.
 *
 * The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 */
public class Sum3Closest {
    public int threeSumClosest(int[] num, int target) {
        if (null == num || num.length < 3) {
            return -1;
        }

        //may introduce problems if arrays contain Integer.MAX_VALUE and Integer.MIN_VALUE
        int sum = 1000000;
        Arrays.sort(num);
        for (int i = 0; i < num.length - 2; i++) {
            int l = i + 1, r = num.length - 1;
            int newTarget = target - num[i];
            while (l < r) {
                int localSum = num[l] + num[r];
                if (Math.abs(sum - target) > Math.abs(newTarget - localSum)) {
                    sum = localSum + num[i];
                }
                if (localSum == newTarget) {
                    return target;
                } else if (localSum < newTarget) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Sum3Closest sum3Closest = new Sum3Closest();
        int[] num = {1,1,1,0};
        System.out.println(sum3Closest.threeSumClosest(num, 100));
    }
}
