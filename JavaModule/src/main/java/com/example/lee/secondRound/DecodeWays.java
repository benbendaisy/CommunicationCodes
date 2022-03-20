package com.example.lee.secondRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/28/15.
 *
 * A message containing letters from A-Z is being encoded to numbers using the following mapping:
 *
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * Given an encoded message containing digits, determine the total number of ways to decode it.
 *
 * For example,
 * Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
 *
 * The number of ways decoding "12" is 2.
 */
public class DecodeWays {
    public int numDecodings(String s) {
        if (null == s || s.length() == 0) return 0;
        Map<String, Integer> map = new HashMap<String, Integer>();
        return numDecodings(s, map);
    }

    private int numDecodings(String s, Map<String, Integer> map) {
        if (s.length() == 0) return 1;
        if (map.containsKey(s)) return map.get(s);
        char ch = s.charAt(0);
        int cnt = 0;
        if (ch == '0') {
            return 0;
        } else if (ch > 0 && ch < '3' && s.length() > 1) {
            char c = s.charAt(1);
            if (ch == '1' || (c < '7' && c >= '0')) cnt += numDecodings(s.substring(2), map);
        }
        cnt += numDecodings(s.substring(1), map);
        map.put(s, cnt);
        return cnt;
    }


    public int numDecodingsI(String s) {
        if (null == s) return 0;
        if (s.length() == 0) return 1;
        char ch = s.charAt(0);
        int cnt = 0;
        if (ch == '0') {
            return 0;
        } else if (ch > 0 && ch < '3' && s.length() > 1) {
            char c = s.charAt(1);
            if (ch == '1' || (c < '7' && c >= '0')) cnt += numDecodingsI(s.substring(2));
        }
        cnt += numDecodings(s.substring(1));
        return cnt;
    }
}
