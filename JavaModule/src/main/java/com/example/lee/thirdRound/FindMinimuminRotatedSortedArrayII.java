package com.example.lee.thirdRound;

public class FindMinimuminRotatedSortedArrayII {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int min = nums[0];
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            min = Math.min(min, nums[l]);
            min = Math.min(min, nums[r]);
            min = Math.min(min, nums[m]);
            if (nums[l] < nums[m] && nums[m] < nums[r]) {
                r = m - 1;
            } else if (nums[r] < nums[m] && nums[m] < nums[l]) {
                l = m + 1;
            } else {
                l++;
                r--;
            }
        }
        return min;
    }
}
