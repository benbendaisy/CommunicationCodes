package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/5/15.
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
 *
 * refer to http://blog.csdn.net/u011095253/article/details/9248073
 */
public class InterleavingString {

    //dp way to solve the problem
    public boolean isInterleave(String s1, String s2, String s3) {
        if(s1 == null || s2 == null || s3 == null || (s1.length() + s2.length() != s3.length())){
            return false;
        }

        int len1 = s1.length();
        int len2 = s2.length();

        //dp is used to store matching from s1 (row) and s2 (column) to s3
        boolean[][] dp = new boolean[len1 + 1][len2 + 1];

        //initial the dp
        //a matching is valid only when current character equals and its previous
        //character matches
        dp[0][0] = true;
        for(int i = 1; i <= len1; i++){
            if(s1.charAt(i - 1) == s3.charAt(i - 1) && dp[i - 1][0]){
                dp[i][0] = true;
            } else {
                dp[i][0] = false;
            }
        }

        for(int j = 1; j <= len2; j++){
            if(s2.charAt(j - 1) == s3.charAt(j - 1) && dp[0][j - 1]){
                dp[0][j] = true;
            } else {
                dp[0][j] = false;
            }
        }

        for(int i = 1; i <= len1; i++){
            for(int j = 1; j <= len2; j++){
                if(s1.charAt(i - 1) == s3.charAt(i + j - 1) && dp[i - 1][j]){
                    dp[i][j] = true;
                }

                if(s2.charAt(j - 1) == s3.charAt(i + j - 1) && dp[i][j - 1]){
                    dp[i][j] = true;
                }
            }
        }

        return dp[len1][len2];
    }

    //recursive way
    public boolean isInterleaveI(String s1, String s2, String s3) {
        if(s1 == null || s2 == null || s3 == null || (s1.length() + s2.length() != s3.length())){
            return false;
        }
        return isInterleave(s1, s2, s3, 0, 0, 0);
    }

    private boolean isInterleave(String s1, String s2, String s3, int l1, int l2, int l3){
        int len1 = s1.length();
        int len2 = s2.length();
        int len3 = s3.length();
        if(l1 >= len1 || l2 >= len2 || l3 >= len3 || l1 + l2 != l3){
            return false;
        } else if(l1 == len1 && l2 == len2 && l3 == len3){
            return true;
        } else if(l1 == len1){
            return s2.substring(l2).equals(s3.substring(l3));
        } else if(l2 == len2){
            return s1.substring(l1).equals(s3.substring(l3));
        } else if(s1.charAt(l1) == s3.charAt(l3) && s2.charAt(l2) == s3.charAt(l3)){
            return isInterleave(s1, s2, s3, l1 + 1, l2, l3 + 1) || isInterleave(s1, s2, s3, l1, l2 + 1, l3 + 1);
        } else if(s1.charAt(l1) == s3.charAt(l3)){
            return isInterleave(s1, s2, s3, l1 + 1, l2, l3 + 1);
        } else if(s2.charAt(l2) == s3.charAt(l3)){
            return isInterleave(s1, s2, s3, l1, l2 + 1, l3 + 1);
        }
        return false;
    }
}
