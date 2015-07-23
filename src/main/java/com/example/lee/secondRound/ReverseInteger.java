package com.example.lee.secondRound;

/**
 * Created by pzhong1 on 6/23/15.
 *
 * Reverse digits of an integer.
 *
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 */
public class ReverseInteger {
    public int reverse(int x) {
        boolean isNegtive = x < 0;
        if (x == Integer.MIN_VALUE) return 0;
        if (isNegtive) x = -x;
        int res = 0;
        while (x > 0) {
            if (canMul(res, 10) && canAdd(res * 10, x % 10)) {
                res = res * 10 + x % 10;
            } else {
                return 0;
            }
            x /= 10;
        }

        return isNegtive ? -res : res;
    }

    private boolean canMul(int x, int y) {
        return Integer.MAX_VALUE / x <= y;
    }

    private boolean canAdd(int x, int y) {
        return Integer.MAX_VALUE - x <= y;
    }

    public static void main(String[] args) {
        ReverseInteger reverseInteger = new ReverseInteger();
        System.out.println(reverseInteger.reverse(-123));
    }
}
