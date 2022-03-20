package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/1/17.
 */
public class RemoveDuplicatesfromSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        } else if (nums.length == 1) {
            return 1;
        }
        int l = 0;
        int r = 0;
        while (r < nums.length) {
            while (r < nums.length - 1 && nums[r] == nums[r + 1]) {
                r++;
            }
            nums[l] = nums[r];
            l++;
            r++;
        }
        return l;
    }
}
