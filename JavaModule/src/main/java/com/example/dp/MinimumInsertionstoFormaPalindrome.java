package com.example.dp;

/**
 * Created by benbendaisy on 5/1/15.
 *
 * Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
 *
 * refer to: http://www.geeksforgeeks.org/dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/
 */
public class MinimumInsertionstoFormaPalindrome {
    public int palindrome(String str) {
        if (null == str || str.length() < 2) return 0;
        int len = str.length();
        int[][] dp = new int[len][len];
        for (int gap = 1; gap < len; gap++) {
            for (int i = 0, j = gap; j < len; j++, i++) {
                if (str.charAt(i) == str.charAt(j)) {
                    dp[i][j] = dp[i + 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][len - 1];
    }

    public int findMinimalInsertion(String str) {
        if (null == str || str.length() < 2) return 0;
        int len = str.length();
        if (str.charAt(0) == str.charAt(len - 1)) {
            return findMinimalInsertion(str.substring(1, len - 1));
        } else {
            return Math.min(findMinimalInsertion(str.substring(1)), findMinimalInsertion(str.substring(0, len - 1))) + 1;
        }
    }

    public static void main(String[] args) {
        MinimumInsertionstoFormaPalindrome mifp = new MinimumInsertionstoFormaPalindrome();
        System.out.println(mifp.palindrome("Ab3bd"));
        System.out.println(mifp.findMinimalInsertion("Ab3bd"));
        System.out.println(mifp.palindrome("abcd"));
        System.out.println(mifp.findMinimalInsertion("abcd"));
    }
}
