package com.example.lee.thirdRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class ThreeSumClosest {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length < 3) {
            return 0;
        }
        Arrays.sort(nums);
        int closedSum = target < 0 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        for (int i = 0; i <  nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int l = i + 1;
            int r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == target) {
                    return sum;
                } else if (sum < target) {
                    l++;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                } else {
                    r--;
                    while (l < r && nums[r] == nums[r + 1]) {
                        r--;
                    }
                }
                closedSum = Math.abs(closedSum - target) > Math.abs(sum - target) ? sum : closedSum;
            }
        }
        return closedSum;
    }

    public static void main(String[] args) {
        ThreeSumClosest threeSumClosest = new ThreeSumClosest();
        int[] nums = {-3,-2,-5,3,-4};
        System.out.println(threeSumClosest.threeSumClosest(nums, -1));
    }
}
