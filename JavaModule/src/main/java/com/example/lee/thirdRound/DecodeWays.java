package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

public class DecodeWays {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        Map<String, Integer> cached = new HashMap<>();
        return numDecodingsHelper(s, cached);
    }

    public int numDecodingsHelper(String s, Map<String, Integer> cached) {
        if (cached.containsKey(s)) {
            return cached.get(s);
        }
        if (s.length() == 0) {
            return 1;
        } else if (s.charAt(0) == '0') {
            return 0;
        } else if (s.length() < 2) {
            return 1;
        }

        int res = 0;
        if (s.charAt(0) == '1') {
            res = numDecodingsHelper(s.substring(1), cached) + numDecodingsHelper(s.substring(2), cached);
        } else if (s.charAt(0) == '2') {
            if (s.charAt(1) <= '6' && s.charAt(1) >= '0') {
                res = numDecodingsHelper(s.substring(1), cached) + numDecodingsHelper(s.substring(2), cached);
            } else {
                res = numDecodingsHelper(s.substring(1), cached);
            }
        } else {
            res = numDecodingsHelper(s.substring(1), cached);
        }
        cached.put(s, res);
        return res;
    }

    public static void main(String[] args) {
        DecodeWays decodeWays = new DecodeWays();
        System.out.println(decodeWays.numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"));
    }
}
