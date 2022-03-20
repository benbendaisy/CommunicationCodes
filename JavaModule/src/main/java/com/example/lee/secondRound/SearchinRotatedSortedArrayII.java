package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/4/15.
 */
public class SearchinRotatedSortedArrayII {
    public boolean search(int[] nums, int target) {
        if (null == nums) return false;
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target || nums[l] == target || nums[r] == target) {
                return true;
            } else if (nums[mid] < target && target < nums[r]) {
                l = mid + 1;
            } else if (nums[mid] > target && nums[l] < target ) {
                r = mid - 1;
            } else {
                l++;
            }
        }
        return false;
    }
}
