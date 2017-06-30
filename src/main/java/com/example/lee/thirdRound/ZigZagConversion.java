package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 6/22/17.
 */
public class ZigZagConversion {
    public String convert(String s, int numRows) {
        if (s == null || s.length() == 0 || numRows <= 1) {
            return s;
        }
        // 步长
        int step = 2 * (numRows - 1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            for (int j = i; j < s.length(); j += step) {
                sb.append(s.charAt(j));
                // 加上往上走的字符再加进去
                if (i != 0 && i != numRows - 1 && j + step - 2 * i < s.length()) {
                    sb.append(s.charAt(j + step - 2 * i));
                }
            }
        }
        return sb.toString();
    }
}
