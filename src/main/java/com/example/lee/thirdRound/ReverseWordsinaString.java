package com.example.lee.thirdRound;

public class ReverseWordsinaString {
    public String reverseWords(String s) {
        if (s == null || s.length() < 1) {
            return s;
        }

        String[] fields = s.trim().split(" +", -1);
        int l = 0, r = fields.length - 1;
        while (l < r) {
            String t = fields[l];
            fields[l] = fields[r];
            fields[r] = t;
            l++;
            r--;
        }
        return String.join(" ", fields);
    }
}
