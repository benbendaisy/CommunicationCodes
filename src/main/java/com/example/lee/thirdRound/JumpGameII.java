package com.example.lee.thirdRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 7/7/17.
 */
public class JumpGameII {
    /**
     * O(n) solution. refer to http://www.programcreek.com/2014/06/leetcode-jump-game-ii-java/
     * @param nums
     * @return
     */
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int canJump = 0;
        int reach = 0;
        int minJump = 0;
        for (int i = 0; i < nums.length; i++) {
            if (reach < i) {
                minJump++;
                reach = canJump;
            }
            canJump = Math.max(canJump, nums[i] + i);
        }
        // if cannot reach the the end, return 0
        if (canJump < nums.length - 1) {
            return 0;
        }
        return minJump;
    }

    /**
     * O(n^2) dynamic solution but not pass leetcode because of 'Time Limit Exceeded'
     * @param nums
     * @return
     */
    public int jumpI(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int[] dp = new int[nums.length];
        int max = dp[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = i;
            max = Math.max(max, nums[i]);
            for (int j = Math.max(0, i - max); j < i; j++) {
                if (nums[j] + j >= i) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[nums.length - 1];
    }

    public static void main(String[] args) {
        JumpGameII jumpGameII = new JumpGameII();
    }
}
