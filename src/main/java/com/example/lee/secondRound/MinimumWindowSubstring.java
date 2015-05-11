package com.example.lee.secondRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 5/3/15.
 */
public class MinimumWindowSubstring {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length()) return "";
        Map<Character, Integer> tMap = new HashMap<Character, Integer>();
        for (char ch : t.toCharArray()) {
            if (tMap.containsKey(ch)) {
                tMap.put(ch, tMap.get(ch) + 1);
            } else {
                tMap.put(ch, 1);
            }
        }

        int cnt = 0;
        Map<Character, Integer> sMap = new HashMap<Character, Integer>();
        int start = 0, st = 0, min = Integer.MAX_VALUE;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (tMap.containsKey(ch)) {
                if (sMap.containsKey(ch)) {
                    sMap.put(ch, sMap.get(ch) + 1);
                } else {
                    sMap.put(ch, 1);
                }
                if (sMap.get(ch) <= tMap.get(ch)) cnt++;
            }
            if (cnt == t.length()) {
                while (!sMap.containsKey(s.charAt(start)) || sMap.get(s.charAt(start)) > tMap.get(s.charAt(start))) {
                    char c = s.charAt(start);
                    if (tMap.containsKey(c)) sMap.put(c, sMap.get(c) - 1);
                    start++;
                }

                if (i - start + 1 < min) {
                    st = start;
                    min = i - start + 1;
                }
            }
        }
        return st + min <= s.length() ? s.substring(st, st + min) : "";
    }

    public static void main(String[] args) {
        MinimumWindowSubstring minimumWindowSubstring = new MinimumWindowSubstring();
        System.out.println(minimumWindowSubstring.minWindow("abc", "cba"));
    }
}
