package com.example.lee.thirdRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 7/5/17.
 */
public class SearchforARange {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[2];
        Arrays.fill(res, -1);
        if (nums == null || nums.length < 1) {
            return res;
        }
        int l = 0;
        int r = nums.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target) {
                l = mid;
                while(l >= 0 && nums[l] == target) {
                    l--;
                }
                r = mid;
                while (r < nums.length && nums[r] == target) {
                    r++;
                }
                res[0] = l + 1;
                res[1] = r - 1;
                return res;
            } else if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }
}
