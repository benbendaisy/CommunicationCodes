package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/14/15.
 *
 * Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
 *
 * You have the following 3 operations permitted on a word:
 *
 * a) Insert a character
 * b) Delete a character
 * c) Replace a character
 */
public class EditDistance {
    //dp represent the minimal steps from the ith character in word1 to the jth
    //character in word2
    //iterative solution
    public int minDistance(String word1, String word2) {
        if(word1 == null || word2 == null){
            return 0;
        }

        int len1 = word1.length();
        int len2 = word2.length();
        int[][] dp = new int[len1 + 1][len2 + 1];

        //initial the dp when word2 is empty
        for(int i = 0; i <= len1; i++){
            dp[i][0] = i;
        }

        //initial the dp when word1 is empty
        for(int j = 0; j <= len2; j++){
            dp[0][j] = j;
        }


        for(int i = 0; i < len1; i++){
            for(int j = 0; j < len2; j++){
                if(word1.charAt(i) == word2.charAt(j)){
                    dp[i + 1][j + 1] = dp[i][j];
                } else {
                    //delete: dp[i][j + 1] + 1
                    //replace: dp[i][j] + 1
                    //insert: dp[i+1][j] + 1
                    dp[i + 1][j + 1] = Math.min(dp[i][j + 1], Math.min(dp[i + 1][j], dp[i][j])) + 1;
                }
            }
        }
        return dp[len1][len2];
    }

    //recursive solution that does not pass leetcode test
    public int minDistanceI(String word1, String word2) {
        if(word1 == null || word2 == null){
            return 0;
        }
        return minDistance(word1, word2, 0, 0);
    }
    public int minDistance(String word1, String word2, int index1, int index2){
        if(index1 == word1.length() && index2 == word2.length()){
            return 0;
        } else if(index1 == word1.length()){
            return word2.length() - index2;
        } else if(index2 == word2.length()){
            return word1.length() - index1;
        }

        if(word1.charAt(index1) == word2.charAt(index2)){
            return minDistance(word1, word2, index1 + 1, index2 + 1);
        } else {
            int insert = minDistance(word1, word2, index1 + 1, index2) + 1;
            int delete = minDistance(word1, word2, index1, index2 + 1) + 1;
            int replace = minDistance(word1, word2, index1 + 1, index2 + 1) + 1;
            return Math.min(insert, Math.min(delete, replace));
        }
    }

}
