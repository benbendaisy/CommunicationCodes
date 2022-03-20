package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/2/15.
 */
public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        if (null == s || s.length() == 0) return true;
        int left = 0, right = s.length() - 1;
        String str = s.toLowerCase();
        while (right >= left) {
            if (!isAlphaNumeric(str.charAt(left)) || !isAlphaNumeric(str.charAt(right))) {
                if (!isAlphaNumeric(str.charAt(left))) {
                    left++;
                }
                if (!isAlphaNumeric(str.charAt(right))) {
                    right--;
                }
                continue;
            }
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            right--;
            left++;
        }
        return true;
    }

    private boolean isAlphaNumeric(char c) {
        if((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
            return true;
        }
        return false;
    }
}
