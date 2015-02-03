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
            return isMatch(s, p, idx1 + 1, idx2 + 1) || isMatch(s, p, idx1 + 1, idx2);
        } else if('?' == p.charAt(idx2)){
            return isMatch(s, p, idx1 + 1, idx2);
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
            //multiple '*' has the same effect with single '*'
            while(idx2 + 1 < p.length() && '*' == p.charAt(idx2 + 1)){
                idx2++;
            }

            //omit value that does not equal the character in p
            while(idx1 < s.length() && idx2 + 1 < p.length() && s.charAt(idx1) != p.charAt(idx2 + 1)){
                idx1++;
            }
            return isMatch(s, p, idx1 + 1, idx2 + 1, map) || isMatch(s, p, idx1 + 1, idx2, map);
        } else if('?' == p.charAt(idx2)){
            return isMatch(s, p, idx1 + 1, idx2, map);
        } else{
            if(s.charAt(idx1) == p.charAt(idx2)){
                return isMatch(s, p, idx1 + 1, idx2 + 1, map);
            } else {
                map.put(s.substring(idx1) + p.substring(idx2), false);
                return false;
            }
        }
    }

    public static void main(String[] args) {
        WildcardMatching wildcardMatching = new WildcardMatching();
        System.out.println(wildcardMatching.isMatchI("abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
                "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"));
    }
}
