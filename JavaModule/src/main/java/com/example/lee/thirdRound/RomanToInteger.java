package com.example.lee.thirdRound;

public class RomanToInteger {
    public int romanToInt(String s) {
        if (s == null || s.length() < 1) {
            return 0;
        }
        int idx = s.length() - 1;
        int res = 0;
        while (idx > 0) {
            int right = charToInt(s.charAt(idx));
            int left = charToInt(s.charAt(idx - 1));
            if (right <= left) {
                res += right;
                idx--;
            } else {
                res += right - left;
                idx -= 2;
            }
        }
        if (idx == 0) {
            res += charToInt(s.charAt(idx));
        }
        return res;
    }
    private int charToInt(char ch) {
        switch (ch) {
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
