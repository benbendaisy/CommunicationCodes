package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/3/15.
 */
public class IntegertoRoman {
    public String intToRoman(int num) {
        if (num < 1 || num > 3999) {
            return "";
        }

        int[] A = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] B = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        while (idx < A.length) {
            while (num >= A[idx]) {
                sb.append(B[idx]);
                num -= A[idx];
            }
            idx++;
        }
        return sb.toString();
    }
}
