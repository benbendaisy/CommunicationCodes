package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/17/15.
 */
public class RomanToInt {
    public int romanToInt(String s) {
        if (null == s || s.length() < 1) return 0;
        int res = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            int l = charToInt(s.charAt(i));
            int r = charToInt(s.charAt(i + 1));
            res += l < r ? -l : l;
        }
        res += charToInt(s.charAt(s.length() - 1));
        return res;
    }

    private int charToInt(char ch) {
        switch(ch) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
        }
        return 0;
    }
}
