package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 7/7/17.
 */
public class WildcardMatching {
    /**
     * recursive + memoirization should be correct but fail leetCode because of 'Time Limit Exceeded'
     * @param s
     * @param p
     * @return
     */
    public boolean isMatchI(String s, String p) {
        if (s == null || p == null) {
            return false;
        }
        Map<String, Map<String, Boolean>> map = new HashMap<>();
        return isMatch(s, p, map);
    }

    private boolean isMatch(String s, String p, Map<String, Map<String, Boolean>> map) {
        if (map.containsKey(s) && map.get(s).containsKey(p)) {
            return map.get(s).get(p);
        }
        if (p.length() == 0 && s.length() == 0) {
            return true;
        } else if (p.length() == 0) {
            return false;
        } else if (s.length() == 0) {
            boolean res = (p.length() == 1 && p.charAt(0) == '*') || (p.charAt(0) == '*' && isMatch(s, p.substring(1), map)) ? true : false;
            Map<String, Boolean> stringBooleanMap = map.getOrDefault(s, new HashMap<>());
            stringBooleanMap.put(p, res);
            map.put(s, stringBooleanMap);
            return res;
        }

        boolean res = false;
        if (s.charAt(0) == p.charAt(0) || p.charAt(0) == '?') {
            res = isMatch(s.substring(1), p.substring(1), map);
        } else if (p.charAt(0) == '*') {
            res = isMatch(s, p.substring(1), map) || isMatch(s.substring(1), p, map) || isMatch(s.substring(1), p.substring(1), map);
        }
        Map<String, Boolean> stringBooleanMap = map.getOrDefault(s, new HashMap<>());
        stringBooleanMap.put(p, res);
        map.put(s, stringBooleanMap);
        return res;
    }

    public boolean isMatch(String s, String p) {
        if (s == null && p == null) {
            return true;
        } else if (s == null || p == null) {
            return false;
        }
        boolean hasStar = false;
        int oldIdxS = 0, curIdxS = 0;
        int oldIdxP = 0, curIdxP = 0;
        while (curIdxS < s.length()) {
            if (curIdxP < p.length() && (s.charAt(curIdxS) == p.charAt(curIdxP) || p.charAt(curIdxP) == '?')) {
                curIdxS++;
                curIdxP++;
            } else if (curIdxP < p.length() && p.charAt(curIdxP) == '*') {
                hasStar = true;
                oldIdxS = curIdxS;
                oldIdxP = curIdxP;
                curIdxP++;
//                oldIdxS++;
            } else if (hasStar) {
                curIdxS = ++oldIdxS;
                curIdxP = oldIdxP + 1;
            } else {
                return false;
            }
        }

        while (curIdxP < p.length() && p.charAt(curIdxP) == '*') {
            curIdxP++;
        }

        return curIdxP == p.length();
    }
    public static void main(String[] args) {
        WildcardMatching wildcardMatching = new WildcardMatching();
        System.out.println(wildcardMatching.isMatch("aa",
                "*"));
    }
}
