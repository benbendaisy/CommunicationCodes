package com.example.dp;

/**
 * Created by benbendaisy on 5/2/15.
 */
public class CountNumberofWaystoReachaGivenScoreInaGame {
    int count(int n, int[] cands) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 0; i < cands.length; i++) {
            for (int j = cands[i]; j <= n; j++) {
                dp[j] += dp[j - cands[i]];
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int[] cands = {3, 5, 10};
        CountNumberofWaystoReachaGivenScoreInaGame cnw = new CountNumberofWaystoReachaGivenScoreInaGame();
        int n = 20;
        System.out.println(String.format("Count for %d is %d\n", n, cnw.count(n, cands)));
        n = 13;
        System.out.println(String.format("Count for %d is %d\n", n, cnw.count(n, cands)));
    }
}
