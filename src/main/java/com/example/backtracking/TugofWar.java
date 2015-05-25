package com.example.backtracking;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/22/15.
 */
public class TugofWar {
    public void towUtil(int[] nums) {
        if (null == nums) return;
        int sum = 0;
        for (int num : nums) sum += num;
        boolean[] cands = new boolean[nums.length];
        boolean[] sln = new boolean[nums.length];
        int[] minDiff = new int[1];
        minDiff[0] = Integer.MAX_VALUE;
        towUtil(nums, cands, minDiff, 0, sum, 0, 0, sln);
        for (int i = 0; i < nums.length; i++) {
            if (sln[i]) System.out.println(nums[i]);
        }

        System.out.println(minDiff[0]);
    }

    private void towUtil(int[] nums, boolean[] cands, int[] minDiff, int idx, int sum, int curSum, int selElement, boolean[] sln) {
        if (idx == nums.length) return;
        //to limit half of the numbers
        //if (selElement > nums.length / 2) return;
        towUtil(nums, cands, minDiff, idx + 1, sum, curSum, selElement, sln);

        // add the current element to the solution
        selElement++;
        curSum += nums[idx];
        cands[idx] = true;
        //to limit half of the numbers
//        if (selElement == nums.length / 2) {
//            if (Math.abs(sum / 2 - curSum) < minDiff[0]) {
//                minDiff[0] = Math.abs(sum / 2 - curSum);
//                for (int i = 0; i < cands.length; i++) {
//                    sln[i] = cands[i];
//                }
//            }
//        } else {
//            towUtil(nums, cands, minDiff, idx + 1, sum, curSum, selElement, sln);
//        }

        // checks if a solution is formed
        if (Math.abs(sum / 2 - curSum) < minDiff[0]) {
            minDiff[0] = Math.abs(sum / 2 - curSum);
            for (int i = 0; i < cands.length; i++) {
                sln[i] = cands[i];
            }
        } else {
            towUtil(nums, cands, minDiff, idx + 1, sum, curSum, selElement, sln);
        }
        cands[idx] = false;
    }

    public static void main(String[] args) {
        TugofWar tugofWar = new TugofWar();
        int[] arr = {23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4};
        tugofWar.towUtil(arr);
    }

}
