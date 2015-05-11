package com.example.lee.secondRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/30/15.
 *
 * Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
 */
public class ScrambleString {
    public boolean isScramble(String s1, String s2) {
        if ((null == s1 && null == s2) || (s1.length() == 0 && s2.length() == 0) || s1.equals(s2)) {
            return true;
        } else if (null == s1 || null == s2 || s1.length() == 0 || s2.length() == 0 || s1.length() != s2.length() || !isSameString(s1, s2)) {
            return false;
        }
        int len = s1.length();
        for (int i = 1; i < len; i++) {
            String s11 = s1.substring(0, i);
            String s12 = s1.substring(i);
            String s21 = s2.substring(0, i);
            String s22 = s2.substring(i);
            if (isScramble(s11, s21) && isScramble(s12, s22)) return true;
            s21 = s2.substring(len - i, len);
            s22 = s2.substring(0, len - i);
            if (isScramble(s11, s21) && isScramble(s12, s22)) return true;
        }
        return false;
    }

    private boolean isSameString(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < s1.length(); i++) {
            char ch = s1.charAt(i);
            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
            }
        }
        for (int i = 0; i < s2.length(); i++) {
            char ch = s2.charAt(i);
            if (!map.containsKey(ch) || map.get(ch) < 1) {
                return false;
            }
            map.put(ch, map.get(ch) - 1);
        }
        return true;
    }

    public static void main(String[] args) {
        ScrambleString scrambleString = new ScrambleString();
        System.out.println(scrambleString.isScramble("ab", "ba"));
    }
}
