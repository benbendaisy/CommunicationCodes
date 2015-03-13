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
}
