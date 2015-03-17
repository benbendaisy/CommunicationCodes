package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/14/15.
 */
public class ReverseWordsinaString {
    public String reverseWords(String s) {
        s = s.trim();
        s = s.replaceAll("\\s+", " ");
        if(s.length() == 0 || s.length() == 1) {
            return s;
        }
        int left = 0, right = s.length() - 1;
        char[] c = s.toCharArray();
        while(left < right){
            char temp = c[left];
            c[left] = c[right];
            c[right] = temp;
            left++;
            right--;
        }

        left = right = 0;
        while( left < s.length()){
            while(right < s.length() && c[right] != ' '){
                right++;
            }
            int tempIndex = right + 1;
            if((right-1) != left){
                right--;
            } else {
                left = right = tempIndex;
                continue;
            }
            while(left < right){
                char temp = c[left];
                c[left] = c[right];
                c[right] = temp;
                left++;
                right--;
            }
            left = right = tempIndex;
        }
        return new String(c);
    }

    //rewrite the program and delete some unnecessary codes
    public String reverseWordsI(String s) {
        if (null == s || s.length() <= 1) {
            return s.trim();
        }

        s = s.trim();
        s = s.replaceAll("\\s+", " ");

        int l = 0, r = s.length() - 1;
        char[] chars = s.toCharArray();
        reverseString(chars, l, r);

        r = 0;
        while (r < chars.length) {
            while (r < chars.length && chars[r] != ' ') {
                r++;
            }
            r--;
            reverseString(chars, l, r);
            r += 2;
            l = r;
        }
        return new String(chars);
    }

    private void reverseString(char[] chars, int l, int r) {
        while (l < r) {
            char ch = chars[l];
            chars[l] = chars[r];
            chars[r] = ch;
            l++;
            r--;
        }
    }
}
