package com.example.lee.thirdRound;

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        if (s == null || s.length() < 2) {
            return true;
        }
        s = s.toLowerCase().trim();
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !isValidCharacter(s.charAt(left))) {
                left++;
            }
            while (left < right && !isValidCharacter(s.charAt(right))) {
                right--;
            }
            if (left < right && s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private boolean isValidCharacter(char ch) {
        return (ch >= '0' && ch <= '9') || (ch >= 'a' && ch <= 'z');
    }
}
