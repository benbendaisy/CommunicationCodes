package com.example.lee.thirdRound;

import java.util.Map;

/**
 * Created by benbendaisy on 6/26/17.
 */
public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int dec = 0;
        int div = 1;
        while (x / div >= 10) {
            div *= 10;
        }

        while (x > 0) {
            int l = x / div;
            int r = x % 10;
            if (l != r) {
                return false;
            }
            x = (x % div) / 10;
            div /= 100;
        }
        return true;
    }

    public static void main(String[] args) {
        PalindromeNumber palindromeNumber = new PalindromeNumber();
        System.out.println(palindromeNumber.isPalindrome(10021));
    }
}
