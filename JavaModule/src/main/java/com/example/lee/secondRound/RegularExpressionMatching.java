package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/16/15.
 *
 * Implement regular expression matching with support for '.' and '*'.
 *
 * '.' Matches any single character.
 * '*' Matches zero or more of the preceding element.
 *
 * The matching should cover the entire input string (not partial).
 *
 * The function prototype should be:
 * bool isMatch(const char *s, const char *p)
 *
 * Some examples:
 * isMatch("aa","a") → false
 * isMatch("aa","aa") → true
 * isMatch("aaa","aa") → false
 * isMatch("aa", "a*") → true
 * isMatch("aa", ".*") → true
 * isMatch("ab", ".*") → true
 * isMatch("aab", "c*a*b") → true
 *
 *
 */
public class RegularExpressionMatching {
    public boolean isMatch(String s, String p) {
        if (null == s || null == p) return false;
        if (s.length() == 0 && p.length() == 0) return true;
        if (s.length() == 0 || p.length() == 0) return false;
        if (p.length() > 1) {
            if (p.charAt(1) != '*') {
                if (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.') {
                    return isMatch(s.substring(1), p.substring(1));
                } else {
                    return false;
                }
            } else {
                if (s.charAt(0) != p.charAt(0) && p.charAt(0) != '.') return false;
                int idx = 1;
                while ((s.charAt(idx) == p.charAt(0) || p.charAt(0) == '.')) {
                    if (isMatch(s.substring(idx), p.substring(2))) return true;
                    idx++;
                }
            }
        } else {
            if (s.length() > 1) {
                return false;
            } else {
                return s.charAt(0) == p.charAt(0) || p.charAt(0) == '.';
            }
        }

        return false;
    }
}
