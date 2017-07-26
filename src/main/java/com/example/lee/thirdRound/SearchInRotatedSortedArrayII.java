package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/16/17.
 */
public class SearchInRotatedSortedArrayII {
    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length < 1) {
            return false;
        }
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (nums[m] == target || nums[l] == target || nums[r] == target) {
                return true;
            } else if (nums[l] < target && target < nums[m]) {
                r = m - 1;
            } else if (nums[m] < target && target < nums[r]) {
                l = m + 1;
            } else {
                l++;
            }
        }
        return false;
    }
}
