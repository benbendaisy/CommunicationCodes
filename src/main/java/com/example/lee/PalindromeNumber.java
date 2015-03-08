package com.example.lee;

/**
 * Created by benbendaisy on 3/3/15.
 *
 * Determine whether an integer is a palindrome. Do this without extra space.
 */
public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int div = 1;
        while (x/div >= 10) {
            div *= 10;
        }

        while (x > 0) {
            int l = x / div;
            int r = x % 10;
            if (l != r) {
                return false;
            } else {
                x = (x % div) / 10;
                div /= 100;
            }
        }

        return true;
    }
}
