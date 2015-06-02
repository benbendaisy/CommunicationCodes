package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/1/15.
 *
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 *
 * Each element in the array represents your maximum jump length at that position.
 *
 * Determine if you are able to reach the last index.
 *
 * For example:
 * A = [2,3,1,1,4], return true.
 *
 * A = [3,2,1,0,4], return false.
 */
public class JumpGame {
    public boolean canJump(int[] nums) {
        if (null == nums || nums.length == 0) return false;
        int maxStep = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (maxStep < 1) return false;
            maxStep--;
            if (maxStep < nums[i]) maxStep = nums[i];
        }
        return true;
    }
}
