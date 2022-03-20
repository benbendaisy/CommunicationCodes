package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/6/15.
 */
public class PalindromePartitioningII {
    //one dimension dp
    public int minCut(String s) {
        if (null == s || s.length() < 2) return 0;
        int len = s.length();
        boolean[][] isPalindrome = new boolean[len][len];
        int[] cuts = new int[len];
        for (int i = 0; i < len; i++) {
            cuts[i] = i;
            for (int j = 0; j <= i; j++) {
                if ((s.charAt(i) == s.charAt(j)) && ((i - j <= 1) || isPalindrome[i - 1][j + 1])) {
                    isPalindrome[i][j] = true;
                    if (j > 0) {
                        cuts[i] = Math.min(cuts[i], cuts[j - 1] + 1);
                    } else {
                        cuts[i] = 0;
                    }
                }
            }
        }
        return cuts[len - 1];
    }
}
