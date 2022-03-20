package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/5/17.
 */
public class SearchInRotatedSortedArray {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = (l + r)/2;
            if (nums[mid] == target) {
                return mid;
            } else if (target > nums[l] && target < nums[mid]) {
                r = mid - 1;
            } else if (target > nums[mid] && target < nums[r]) {
                l = mid + 1;
            } else {
                if (nums[l] == target){
                    return l;
                } else if (nums[r] == target) {
                    return r;
                }
                l++;
            }
        }
        return -1;
    }
}
