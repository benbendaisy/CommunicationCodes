package com.example.lee;

/**
 * Created by benbendaisy on 3/3/15.
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
 */

//refer to http://www.programcreek.com/2012/12/leetcode-regular-expression-matching-in-java/
public class RegularExpressionMatching {
//    public boolean isMatch(String s, String p) {
//        if (null == s || null == p) {
//            return false;
//        }
//
//        int idxs = 0, idxp = 0;
//        int oIdxs = 0, oIdxp = 0;
//        boolean hasStar = false;
//        while (idxs < s.length() && idxp < p.length()) {
//            char ch = p.charAt(idxp);
//            switch (ch) {
//                case '*': hasStar = true; oIdxs = idxs; idxp++; oIdxp = idxp;
//                    break;
//                case '.': idxs++; idxp++;
//                    break;
//                default:
//                    if (s.charAt(idxs) != p.charAt(idxp)) {
//                        if (hasStar) {
//                            oIdxs++;
//                            idxs = oIdxs;
//                            idxp = oIdxp;
//                        } else {
//                            return false;
//                        }
//                    } else {
//                        idxp++;
//                        idxs++;
//                    }
//            }
//        }
//
//        return idxs == s.length() && idxp == p.length() ? true : false;
//    }


    public boolean isMatch(String s, String p) {
        if ((null == s && null == p) || p.equals(s)) {
            return true;
        } else if (null == s || null == p) {
            return false;
        } else if (p.length() == 0) {
            return s.length() == 0;
        } else if (s.length() == 0) {
            //handle a* repeating pattern
            if (p.length() >= 2 && p.charAt(1) == '*') {
                return isMatch(s, p.substring(2));
            } else {
                return false;
            }
        }

        //handle .* case and .
        if (p.charAt(0) == '.' && p.length() >= 2 && p.charAt(1) == '*') {
            int i = 0;
            while (i < s.length()) {
                if (isMatch(s.substring(i + 1), p.substring(2))) {
                    return true;
                }
                i++;
            }
        } else if (p.charAt(0) == '.') {
            return isMatch(s.substring(1), p.substring(1));
        }

        //hand current characters equal
        if (s.charAt(0) == p.charAt(0)) {
            //handle *
            if (p.length() >= 2 && p.charAt(1) == '*') {
                int i = -1;
                while (i < 0 || (i < s.length() && s.charAt(i) == p.charAt(0))) {
                    //here will introduce duplicate trip and time out
                    if (isMatch(s.substring(i + 1), p.substring(2))) {
                        return true;
                    }
                    i++;
                }
            } else {
                return isMatch(s.substring(1), p.substring(1));
            }
        } else {
            //handle current character not equal
            if (p.length() >= 2 && p.charAt(1) == '*') {
                return isMatch(s, p.substring(2));
            } else {
                return false;
            }
        }

        return false;
    }

    //merge two conditions in methods above
    public boolean isMatchI(String s, String p) {
        if ((null == s && null == p) || s.equals(p)) {
            return true;
        } else if (null == s || null == p) {
            return false;
        } else if (p.length() == 0) {
            return s.length() == 0;
        }

        //handle two cases, 1) second character in p is not '*' 2) second character in p is '*'
        if (p.length() == 1 || p.charAt(1) != '*') {
            //when first characters do not equal
            if (s.length() < 1 || (s.charAt(0) != p.charAt(0) && p.charAt(0) != '.')) {
                return false;
            } else {
                return isMatchI(s.substring(1), p.substring(1));
            }
        } else if (p.length() > 1 && p.charAt(1) == '*') {
            int i = -1;
            //iteratively compare character in s and p as a* can be zero or mor
            while (i < s.length() && (i < 0 || s.charAt(i) == p.charAt(0) || p.charAt(0) == '.')) {
                if (isMatchI(s.substring(i + 1), p.substring(2))) {
                    return true;
                }
                i++;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        RegularExpressionMatching regularExpressionMatching = new RegularExpressionMatching();
        System.out.println(regularExpressionMatching.isMatchI("aa", "a*"));
    }
}
