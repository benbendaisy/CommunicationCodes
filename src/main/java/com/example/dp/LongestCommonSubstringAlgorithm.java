package com.example.dp;

/**
 * Created by benbendaisy on 3/7/15.
 */
public class LongestCommonSubstringAlgorithm {
    public String lcs(String str1, String str2) {
        if (null == str1 || null == str2 || str1.length() == 0 || str2.length() == 0) {
            return "";
        }

        int row = str1.length();
        int col = str2.length();

        int[][] arr = new int[row + 1][col + 1];
        int len = -1, idx = -1;
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                    arr[i][j] = arr[i - 1][j - 1] + 1;
                    if (arr[i][j] > len) {
                        len = arr[i][j];
                        idx = i;
                    }
                } else {
                    arr[i][j] = 0;
                }
            }
        }

        if (len != -1) {
            return str1.substring(idx - len, idx);
        } else {
            return "";
        }
    }

    public static void main(String[] args) {
        LongestCommonSubstringAlgorithm longestCommonSubstringAlgorithm = new LongestCommonSubstringAlgorithm();
        System.out.println(longestCommonSubstringAlgorithm.lcs("abacdfgdcaba", "hij"));
    }
}
