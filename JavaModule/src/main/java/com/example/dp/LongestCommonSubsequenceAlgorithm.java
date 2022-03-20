package com.example.dp;

/**
 * Created by benbendaisy on 5/1/15.
 */
public class LongestCommonSubsequenceAlgorithm {
    public int lcs(String str1, String str2) {
        if (null == str1 || null == str2 || str1.length() == 0 || str2.length() == 0) {
            return 0;
        }

        int row = str1.length();
        int col = str2.length();

        int[][] arr = new int[row + 1][col + 1];
        int len = -1, idx = -1;
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                    arr[i][j] = arr[i - 1][j - 1] + 1;
                } else {
                    arr[i][j] = Math.max(arr[i - 1][j], arr[i][j - 1]);
                }
            }
        }
        return arr[row][col];
    }
    public static void main(String[] args) {
        LongestCommonSubstringAlgorithm longestCommonSubstringAlgorithm = new LongestCommonSubstringAlgorithm();
        LongestCommonSubsequenceAlgorithm longestCommonSubsequenceAlgorithm = new LongestCommonSubsequenceAlgorithm();
        System.out.println(longestCommonSubstringAlgorithm.lcs("ABCBDAB", "BDCABC"));
        System.out.println(longestCommonSubsequenceAlgorithm.lcs("ABCBDAB", "BDCABC"));

    }
}
