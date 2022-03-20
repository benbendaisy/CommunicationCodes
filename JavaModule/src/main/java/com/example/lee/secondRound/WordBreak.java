package com.example.lee.secondRound;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Created by benbendaisy on 3/30/15.
 */
public class WordBreak {
    //recursive
    public boolean wordBreak(String s, Set<String> dict) {
        if (null == s || dict.contains(s)) return true;
        for (int i = 1; i < s.length(); i++) {
            String subStr = s.substring(0, i);
            if (dict.contains(subStr) && wordBreak(s.substring(i), dict)) {
                return true;
            }
        }
        return false;
    }

    //recursive with memorization
    public boolean wordBreakI(String s, Set<String> dict) {
        if (null == s || dict.contains(s)) return true;
        Map<String, Boolean> map = new HashMap<String, Boolean>();
        return wordBreak(s, dict, map);
    }

    public boolean wordBreak(String s, Set<String> dict, Map<String, Boolean> map) {
        if (null == s || dict.contains(s)) return true;
        if (map.containsKey(s)) return map.get(s);
        for (int i = 1; i < s.length(); i++) {
            String lStr = s.substring(0, i);
            String rStr = s.substring(i);
            if (dict.contains(lStr) && wordBreak(rStr, dict, map)) {
                map.put(s, true);
                return true;
            }
        }
        map.put(s, false);
        return false;
    }

    //dp with iterative way
    public boolean wordBreakII(String s, Set<String> dict) {
        if (null == s || dict.contains(s)) return true;
        boolean[] dp = new boolean[s.length() + 1];
        for (int i = 1; i <= s.length(); i++) {
            String str = s.substring(0, i);
            if (dict.contains(str) && !dp[i]) dp[i] = true;
            if (dp[i]) {
                if (i == s.length()) return true;
                for (int j = i + 1; j <= s.length(); j++) {
                    String subStr = s.substring(i, j);
                    if (dict.contains(subStr) && !dp[j]) dp[j] = true;
                    if (j == s.length() && dp[j]) return true;
                }
            }

        }
        return false;
    }

    public static void main(String[] args) {
        WordBreak wordBreak = new WordBreak();
        Set<String> dict = new HashSet<String>();
        dict.add("a");
        dict.add("aa");
        dict.add("aaa");
        dict.add("aaaa");
        dict.add("aaaaa");
        dict.add("aaaaaa");
        dict.add("aaaaaaa");
        dict.add("aaaaaaaa");
        dict.add("aaaaaaaaa");
        dict.add("aaaaaaaaaa");
        System.out.println(wordBreak.wordBreakII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", dict));
    }
}
