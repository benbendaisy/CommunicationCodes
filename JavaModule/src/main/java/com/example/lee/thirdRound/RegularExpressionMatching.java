package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 6/26/17.
 */
public class RegularExpressionMatching {
    /**
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
     * @param s
     * @param p
     * @return
     */
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) {
            return false;
        }

        if (s.length() == 0) {
            return p.length() == 0 || (p.length() > 1 && p.charAt(1) == '*' && isMatch(s, p.substring(2)));
        }

        if (p.length() >= 1) {
            if (p.length() > 1 && p.charAt(1) == '*') {
                if (s.charAt(0) != p.charAt(0)) {
                    if (p.charAt(0) == '.') {
                        return isMatch(s, p.substring(2)) || isMatch(s.substring(1), p.substring(2)) || isMatch(s.substring(1), p);
                    }
                    return isMatch(s, p.substring(2));
                }
                return isMatch(s, p.substring(2)) || isMatch(s.substring(1), p);
            }

            if (p.charAt(0) == '.' || s.charAt(0) == p.charAt(0)) {
                return isMatch(s.substring(1), p.substring(1));
            }
        }

        return false;
    }

    public boolean isMatchI(String s, String p) {
        if (s == null && p == null) {
            return true;
        } else if (s == null || p == null) {
            return false;
        } else if (s.length() == 0 && p.length() == 0) {
            return true;
        } else if (p.length() == 0) {
            return false;
        } else if (s.length() == 0) {
            return p.length() > 1 && p.charAt(1) == '*' && isMatchI(s, p.substring(2));
        }

        if (p.length() > 1) {
            if (p.charAt(1) == '*') {
                if (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.') {
                    return isMatchI(s, p.substring(2)) || isMatchI(s.substring(1), p.substring(2)) || isMatchI(s.substring(1), p);
                }
                return isMatchI(s, p.substring(2));
            } else if (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.') {
                return isMatchI(s.substring(1), p.substring(1));
            }
        }
        return s.length() == 1 && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.');
    }

    public static void main(String[] args) {
        RegularExpressionMatching regularExpressionMatching = new RegularExpressionMatching();
        System.out.println(regularExpressionMatching.isMatchI("aa", "a"));
        System.out.println(regularExpressionMatching.isMatchI("aa", "aa"));
        System.out.println(regularExpressionMatching.isMatchI("aaa", "aa"));
        System.out.println(regularExpressionMatching.isMatchI("aa", "a*"));
        System.out.println(regularExpressionMatching.isMatchI("aa", ".*"));
        System.out.println(regularExpressionMatching.isMatchI("ab", ".*"));
        System.out.println(regularExpressionMatching.isMatchI("aab", "c*a*b"));
        System.out.println(regularExpressionMatching.isMatchI("bbbba", ".*a*a"));
        System.out.println(regularExpressionMatching.isMatchI("", "c*c*"));
        System.out.println(regularExpressionMatching.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"));
    }
}
