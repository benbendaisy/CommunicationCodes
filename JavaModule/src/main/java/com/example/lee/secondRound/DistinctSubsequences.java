package com.example.lee.secondRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/12/15.
 *
 * Given a string S and a string T, count the number of distinct subsequences of T in S.
 *
 * A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
 *
 * Here is an example:
 * S = "rabbbit", T = "rabbit"
 *
 * Return 3.
 */
public class DistinctSubsequences {
    public int numDistinct(String S, String T) {
        if (null == S || null == T || S.length() < T.length()) return 0;
        int sLen = S.length();
        int tLen = T.length();
        int[][] dp = new int[sLen + 1][tLen + 1];
        for (int i = 0; i <= sLen; i++) {
            dp[i][0] = 1;
        }
        for (int i = 1; i <= sLen; i++) {
            for (int j = 1; j <= tLen; j++) {
                dp[i][j] = dp[i - 1][j];
                if (S.charAt(i - 1) == T.charAt(j - 1)) {
                    dp[i][j] += dp[i - 1][j - 1];
                }
            }
        }
        return dp[sLen][tLen];
    }

    //recursive with memorization did not pass big unit test
    public int numDistinctI(String S, String T) {
        if (null == S || null == T || S.length() < T.length()) return 0;
        Map<String, Integer> map = new HashMap<String, Integer>();
        return numDistinct(S, T, map);
    }

    public int numDistinct(String S, String T, Map<String, Integer> map) {
        if (S.equals(T) || T.length() == 0) {
            return 1;
        } else if (S.length() < T.length()) {
            return 0;
        }
        String str = S + ":" + T;
        if (map.containsKey(str)) {
            return map.get(str);
        }
        int cnt = 0;
        if (S.charAt(0) == T.charAt(0)) {
            cnt = numDistinct(S.substring(1), T.substring(1), map);
        }

        cnt += numDistinct(S.substring(1), T, map);
        map.put(str, cnt);
        return cnt;
    }
}
