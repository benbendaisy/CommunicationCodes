package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/16/15.
 *
 * Implement wildcard pattern matching with support for '?' and '*'.
 *
 * '?' Matches any single character.
 * '*' Matches any sequence of characters (including the empty sequence).
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
 * isMatch("aa", "*") → true
 * isMatch("aa", "a*") → true
 * isMatch("ab", "?*") → true
 * isMatch("aab", "c*a*b") → false
 *
 */
public class WildcardMatching {
    public boolean isMatch(String s, String p) {
        if (null == s && null == p) {
            return true;
        } else if (null == s || null == p) {
            return false;
        }
        boolean hasStar = false;
        int idxs = 0, idxp = 0;
        int oidxs = 0, oidxp = 0;
        int lens = s.length(), lenp = p.length();
        while (idxs < lens) {
            if (idxp < lenp && (s.charAt(idxs) == p.charAt(idxp) || p.charAt(idxp) == '?')) {
                idxs++;
                idxp++;
            } else if (idxp < lenp && p.charAt(idxp) == '*') {
                oidxs = idxs;
                oidxp = idxp;
                hasStar = true;
                idxp++;
            } else if (hasStar) {
                idxs = ++oidxs;
                idxp = oidxp + 1;
            } else {
                return false;
            }
        }
        while (idxp < lenp && p.charAt(idxp) == '*') {
            idxp++;
        }
        return idxp == lenp;
    }

    public static void main(String[] args) {
        WildcardMatching wildcardMatching = new WildcardMatching();
        System.out.println(wildcardMatching.isMatch("aa", "*"));
    }
}
