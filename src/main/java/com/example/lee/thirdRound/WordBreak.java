package com.example.lee.thirdRound;

import java.util.*;

public class WordBreak {
    public boolean wordBreak(String s, List<String> wordDict) {
        if (s == null || s.length() == 0 || wordDict == null || wordDict.isEmpty()) {
            return false;
        }
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        Set<String> dict = new HashSet<>(wordDict);
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j]) {
                    String subString = s.substring(j, i);
                    if (dict.contains(subString)) {
                        dp[i] = true;
                        break;
                    }
                }

            }
        }
        return dp[s.length()];
    }
    /*
     * dfs + memoinization
     */
    public boolean wordBreakI(String s, List<String> wordDict) {
        if (s == null || s.length() == 0) {
            return false;
        }
        Set<String> dict = new HashSet<>(wordDict);
        return wordBreakHelper(s, dict, 0, new HashMap<>());
    }

    private boolean wordBreakHelper(String s, Set<String> dict, int idx, Map<String, Boolean> cached) {
        if (idx == s.length()) {
            return true;
        }
        String subString = s.substring(idx);
        if (cached.containsKey(subString)) {
            return cached.get(subString);
        }
        for (int i = idx + 1; i <= s.length(); i++) {
            if (dict.contains(s.substring(idx, i)) && wordBreakHelper(s, dict, i, cached)) {
                return true;
            }
        }
        cached.put(subString, false);
        return false;
    }

    public static void main(String[] args) {
        WordBreak wordBreak = new WordBreak();
    }
}
