package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/8/15.
 *
 * You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
 *
 * Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
 */
public class HouseRobber {
    public int rob(int[] num) {
        if (null == num || num.length < 1) return 0;
        int[] dp = new int[num.length + 1];
        int max = 0;
        for (int i = 1; i <= num.length; i++) {
            for (int j = 0; j < i - 1; j++) {
                dp[i] = Math.max(dp[j], dp[i]);
            }
            dp[i] += num[i - 1];
            max = Math.max(max, dp[i]);
        }
        return max;
    }

    public static void main(String[] args) {
        int[] num = {2, 1};
        HouseRobber houseRobber = new HouseRobber();
        System.out.println(houseRobber.rob(num));
    }
}
