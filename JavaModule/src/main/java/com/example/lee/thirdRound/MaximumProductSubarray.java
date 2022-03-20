package com.example.lee.thirdRound;

public class MaximumProductSubarray {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        left[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (left[i - 1] == 0) {
                left[i] = nums[i];
            } else {
                left[i] = left[i - 1] * nums[i];
            }
        }
        right[nums.length - 1] = nums[nums.length - 1];
        int max = Math.max(left[0], nums[nums.length - 1]); // set the max to the first element
        for (int i = nums.length - 2; i >= 0; i--) {
            if (right[i + 1] == 0) {
                right[i] = nums[i];
            } else {
                right[i] = right[i + 1] * nums[i];
            }
            max = Math.max(max, left[i]);
            max = Math.max(max, right[i]);
            max = Math.max(max, left[i] * right[i + 1]);
        }
        return max;
    }
}
