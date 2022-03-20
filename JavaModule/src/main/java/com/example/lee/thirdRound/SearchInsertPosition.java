package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/5/17.
 */
public class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                if (mid == 0 || nums[mid - 1] < target) {
                    return mid;
                }
                r = mid - 1;
            } else {
                if (mid == nums.length - 1 || nums[mid + 1] > target ) {
                    return mid + 1;
                }
                l = mid + 1;
            }
        }
        return l - 1;
    }
}
