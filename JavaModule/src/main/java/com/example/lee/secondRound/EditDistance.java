package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/11/15.
 */
public class EditDistance {
    public int minDistance(String word1, String word2) {
        if (null == word1 && null == word2) {
            return 0;
        } else if (null == word1) {
            return word2.length();
        } else if (null == word2) {
            return word1.length();
        }
        int len1 = word1.length();
        int len2 = word2.length();
        int[][] dp = new int[len1 + 1][len2 + 1];
        for (int i = 1; i <= len1; i++) {
            dp[i][0] = i;
        }
        for (int j = 1; j <= len2; j++) {
            dp[0][j] = j;
        }
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1);
                    dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j]);
                }
            }
        }
        return dp[len1][len2];
    }
}