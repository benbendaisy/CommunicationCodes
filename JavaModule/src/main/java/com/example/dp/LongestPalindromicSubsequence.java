package com.example.dp;

/**
 * Created by benbendaisy on 6/14/15.
 *
 * Given a sequence, find the length of the longest palindromic subsequence in it.
 *
 * refer to http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/
 */
public class LongestPalindromicSubsequence {
    //recursive way
    public int lps(String s) {
        if (null == s || s.length() < 1) return 0;
        return lps(s, 0, s.length() - 1);
    }

    public int lps(String s, int l, int r) {
        if (l == r) return 1;
        if (s.charAt(l) == s.charAt(r)) {
            if (l + 1 == r) return 2;
            return lps(s, l + 1, r - 1) + 2;
        }
        return Math.max(lps(s, l + 1, r), lps(s, l, r - 1));
    }

    //dp way
    public int lpsI(String s) {
        if (null == s || s.length() < 1) return 0;
        int len = s.length();
        int[][] dp = new int[len][len];
        for (int i = 0; i < len; i++) dp[i][i] = 1;
        for (int gap = 1; gap < len; gap++) {
            for (int i = 0, j = gap; j < len; j++, i++) {
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][len - 1];
    }

    public static void main(String[] args) {
        LongestPalindromicSubsequence longestPalindromicSubsequence = new LongestPalindromicSubsequence();
        System.out.println(longestPalindromicSubsequence.lps("GEEKS FOR GEEKS"));
        System.out.println(longestPalindromicSubsequence.lpsI("GEEKS FOR GEEKS"));
    }

}
