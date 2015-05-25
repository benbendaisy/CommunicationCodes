package com.example.ip;

/**
 * Created by pzhong1 on 5/12/15.
 */
public class MaxmizeSequenceNumber {
    public static int getMaxNum(int[] nums) {
        if (null == nums || nums.length < 1) return 0;
        int len = nums.length;
        int[] dp = new int[len + 1];
        int max = Integer.MIN_VALUE;
        for (int i = 1; i <= len; i++) {
            dp[i] = nums[i - 1];
            //loop to find the maximal nums
            for (int j = 0; j < i - 1; j++) {
                dp[i] = Math.max(dp[j] + nums[i - 1], dp[i]);
            }
            max = Math.max(dp[i], max);
        }
        return max;
    }

    public static int getMaxNumI(int[] nums) {
        if (null == nums || nums.length < 1) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int len = nums.length;
        int max = Integer.MIN_VALUE;
        int prev1 = nums[0], prev2 = nums[1];
        for (int i = 2; i < len; i++) {
            int cur = nums[i] + prev1;
            max = Math.max(cur, max);
            prev1 = prev2;
            prev2 = cur;
        }
        return max;
    }
}
