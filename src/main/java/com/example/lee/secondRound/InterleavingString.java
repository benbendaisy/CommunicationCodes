package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/19/15.
 *
 * Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
 *
 * For example,
 * Given:
 * s1 = "aabcc",
 * s2 = "dbbca",
 *
 * When s3 = "aadbbcbcac", return true.
 * When s3 = "aadbbbaccc", return false.
 */
public class InterleavingString {
    //dp way that passed all tests
    public boolean isInterleave(String s1, String s2, String s3) {
        if (null == s1 && null == s2 && null == s3) {
            return true;
        } else if (null == s1 || null == s2 || null == s3 || s1.length() + s2.length() != s3.length()) {
            return false;
        } else if (s1.length() == 0) {
            return s2.equals(s3);
        } else if (s2.length() == 0) {
            return s1.equals(s3);
        }

        boolean[][] dp = new boolean[s1.length() + 1][s2.length() + 1];
        dp[0][0] = true;
        for (int i = 1; i <= s1.length(); i++) {
            if (s1.charAt(i - 1) == s3.charAt(i - 1) && dp[i - 1][0]) {
                dp[i][0] = true;
            } else {
                dp[i][0] = false;
            }
        }
        for (int j = 1; j <= s2.length(); j++) {
            if (s2.charAt(j - 1) == s3.charAt(j - 1) && dp[0][j - 1]) {
                dp[0][j] = true;
            } else {
                dp[0][j] = false;
            }
        }

        for (int i = 1; i <= s1.length(); i++) {
            for (int j = 1; j <= s2.length(); j++) {
                if (s1.charAt(i - 1) == s3.charAt(i + j - 1) && dp[i - 1][j]) dp[i][j] = true;
                if (s2.charAt(j - 1) == s3.charAt(i + j - 1) && dp[i][j - 1]) dp[i][j] = true;
            }
        }

        return dp[s1.length()][s2.length()];
    }

    public boolean isInterleaveI(String s1, String s2, String s3) {
        if (null == s1 && null == s2 && null == s3) {
            return true;
        } else if (null == s1 || null == s2 || null == s3 || s1.length() + s2.length() != s3.length()) {
            return false;
        } else if (s1.length() == 0) {
            return s2.equals(s3);
        } else if (s2.length() == 0) {
            return s1.equals(s3);
        }

        if (s1.charAt(0) != s3.charAt(0) && s2.charAt(0) != s3.charAt(0)) {
            return false;
        } else {
            if (s1.charAt(0) == s3.charAt(0) && s2.charAt(0) == s3.charAt(0)) {
                return isInterleave(s1.substring(1), s2, s3.substring(1)) || isInterleave(s1, s2.substring(1), s3.substring(1));
            } else if (s1.charAt(0) == s3.charAt(0)) {
                return isInterleave(s1.substring(1), s2, s3.substring(1));
            } else if (s2.charAt(0) == s3.charAt(0)) {
                return isInterleave(s1, s2.substring(1), s3.substring(1));
            } else {
                return false;
            }
        }
    }
}
