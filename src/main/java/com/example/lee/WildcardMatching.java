package com.example.lee;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 2/2/15.
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
 */
public class WildcardMatching {
    public boolean isMatch(String s, String p) {
        if(null == s){
            return null == p ? true : false;
        } else if(null == p){
            return false;
        }
        return isMatch(s, p, 0, 0);
    }

    private boolean isMatch(String s, String p, int idx1, int idx2){
        if(idx1 == s.length()){
            return idx2 == p.length() ? true : false;
        } else if(idx2 == p.length()){
            return false;
        }

        if('*' == p.charAt(idx2)){
            return isMatch(s, p, idx1 + 1, idx2 + 1) || isMatch(s, p, idx1 + 1, idx2) || isMatch(s, p, idx1, idx2 + 1);
        } else if('?' == p.charAt(idx2)){
            return isMatch(s, p, idx1 + 1, idx2 + 1);
        } else{
            if(s.charAt(idx1) == p.charAt(idx2)){
                return isMatch(s, p, idx1 + 1, idx2 + 1);
            } else {
                return false;
            }
        }
    }

    public boolean isMatchI(String s, String p) {
        if(null == s){
            return null == p ? true : false;
        } else if(null == p){
            return false;
        }
        Map<String, Boolean> map = new HashMap<String, Boolean>();
        //Set<Boolean> set = new HashSet<Boolean>();
        return isMatch(s, p, 0, 0, map);
    }

    private boolean isMatch(String s, String p, int idx1, int idx2, Map<String, Boolean> map){
        if(idx1 >= s.length()){
            return idx2 >= p.length() ? true : false;
        } else if(idx2 >= p.length()){
            return false;
        } else if(map.containsKey(s.substring(idx1) + p.substring(idx2))){
            return map.get(s.substring(idx1) + p.substring(idx2));
        }

        if('*' == p.charAt(idx2)){
//            //multiple '*' has the same effect with single '*'
//            while(idx2 + 1 < p.length() && '*' == p.charAt(idx2 + 1)){
//                idx2++;
//            }
//
//            //omit value that does not equal the character in p
//            while(idx1 < s.length() && idx2 + 1 < p.length() && s.charAt(idx1) != p.charAt(idx2 + 1)){
//                idx1++;
//            }
            return isMatch(s, p, idx1 + 1, idx2 + 1, map) || isMatch(s, p, idx1 + 1, idx2, map) || isMatch(s, p, idx1, idx2 + 1, map);
        } else if('?' == p.charAt(idx2)){
            return isMatch(s, p, idx1 + 1, idx2 + 1, map);
        } else{
            if(s.charAt(idx1) == p.charAt(idx2)){
                return isMatch(s, p, idx1 + 1, idx2 + 1, map);
            } else {
                map.put(s.substring(idx1) + p.substring(idx2), false);
                return false;
            }
        }
    }

    //iteratively check
    public boolean isMatchII(String s, String p) {
        if(null == s){
            return null == p ? true : false;
        } else if(null == p){
            return false;
        }

        int idxs = 0;
        int idxp = 0;
        int lens = s.length();
        int lenp = p.length();
        int idxs1 = 0, idxp1 = 0;
        boolean hasStar = false;
        while(idxs < lens && idxp <= lenp){
            //handle the case *?
            if(idxp == lenp){
                if(hasStar){
                    idxp = idxp1;
                    idxs1++;
                    idxs = idxs1;
                } else {
                    return false;
                }
            }
            char ch = p.charAt(idxp);
            switch (ch) {
                case '?': {
                    idxs++;
                    idxp++;
                    break;
                }
                case '*': {
                    hasStar = true;
                    //handle multiple star
                    while(idxp < lenp && '*' == p.charAt(idxp)){
                        idxp++;
                    }
                    //if star is the last character, it match any string
                    if(idxp == lenp){
                        return true;
                    }
                    idxs1 = idxs;
                    idxp1 = idxp;
                    break;
                }
                default: {
                    if(s.charAt(idxs) != p.charAt(idxp)){
                        if(hasStar){
                            //skip one character in string s
                            idxp = idxp1;
                            idxs1++;
                            idxs = idxs1;
                        } else {
                            return false;
                        }
                    } else {
                        idxs++;
                        idxp++;
                    }
                    break;
                }
            }
        }

        while (idxp < lenp && '*' == p.charAt(idxp)) {
            idxp++;
        }

        return idxp == lenp ? true : false;
    }

    public static void main(String[] args) {
        WildcardMatching wildcardMatching = new WildcardMatching();
        System.out.println(wildcardMatching.isMatchI("hi", "*?"));
    }
}
