package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/3/15.
 */
public class RomantoInteger {
    public int romanToInt(String s) {
        if (null == s || s.length() < 1) {
            return -1;
        }
        int idx = s.length() - 1, total = 0;
        while(idx > 0) {
            int right = charToI(s.charAt(idx));
            int left = charToI(s.charAt(idx - 1));
            if (right <= left) {
                total += right;
                idx--;
            } else {
                total += right - left;
                idx -= 2;
            }

        }
        if (idx == 0) {
            total += charToI(s.charAt(idx));
        }
        return total;
    }

    private int charToI(char ch) {
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


    //refer to http://blog.csdn.net/ironyoung/article/details/45225693
    public int romanToIntI(String s) {
        if (null == s || s.length() < 1) {
            return -1;
        }
        int res = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            int l = charToI(s.charAt(i));
            int r = charToI(s.charAt(i + 1));
            if (l < r) {
                res -= l;
            } else {
                res += r;
            }
        }
        res += charToI(s.charAt(s.length() - 1));
        return res;
    }
}
