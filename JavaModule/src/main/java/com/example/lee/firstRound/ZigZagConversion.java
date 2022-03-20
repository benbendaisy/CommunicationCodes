package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/3/15.
 *
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
 *
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * And then read line by line: "PAHNAPLSIIGYIR"
 * Write the code that will take a string and make this conversion given a number of rows:
 *
 * string convert(string text, int nRows);
 * convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
 *
 * refer to http://blog.csdn.net/linhuanmars/article/details/21145039
 *
 * nRows = 2
 * 0 2 4 6 ...
 * 1 3 5 7
 *
 * nRows = 3
 * 0   4   8  ...
 * 1 3 5 7 9
 * 2   6   10
 *
 * nRows = 4
 * 0     6     12 ...
 * 1   5 7   1113
 * 2 4   8 10  14
 * 3     9     15
 *
 */
public class ZigZagConversion {
    public String convert(String s, int nRows) {
        if (null == s || s.length() <= nRows || nRows == 1) {
            return s;
        }
        int zigSize = 2 * nRows - 2;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < nRows; i++) {
            for (int j = i; j < s.length(); j += zigSize) {
                sb.append(s.charAt(j));
                if (i != 0 && i != nRows -1 && j + zigSize -2 * i < s.length()) {
                    sb.append(s.charAt(j + zigSize - 2 * i));
                }
            }
        }

        return sb.toString();
    }
}
