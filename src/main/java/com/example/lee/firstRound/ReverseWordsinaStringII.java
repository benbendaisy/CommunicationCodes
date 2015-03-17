package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/14/15.
 */
public class ReverseWordsinaStringII {
    //assume there no space at the beginning and the end and one space between words
    public void reverseWords(char[] s) {
        reversCharsArray(s, 0, s.length - 1);
        int l = 0, r = 0;
        while (r < s.length) {
            while (r < s.length && s[r] != ' ') {
                r++;
            }
            r--;
            reversCharsArray(s, l, r);
            r += 2;
            l = r;
        }
    }

    private void reversCharsArray(char[] chars, int l, int r) {
        while (l < r) {
            int t = chars[l];
            chars[l] = chars[r];
            l++;
            r--;
        }
    }
}
