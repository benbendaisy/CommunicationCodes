package com.example.lee;

/**
 * Created by benbendaisy on 3/3/15.
 *
 * Reverse digits of an integer.
 *
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 */
public class ReverseInteger {
    public int reverse(int x) {
        boolean isNegative = x < 0 ? true : false;
        if (x == Integer.MIN_VALUE) {
            return 0;
        } else if (isNegative) {
            x = -x;
        }
        int res = 0;
        while (x > 0) {
            if (canMul(res, 10)) {
                res *= 10;
                if (canAdd(res, x % 10)) {
                    res += x % 10;
                } else {
                    return 0;
                }
            } else {
                return 0;
            }
            x /= 10;
        }
        return isNegative ? -res : res;
    }

    private boolean canMul(int x, int y) {
        return Integer.MAX_VALUE / y < x ? false : true;
    }

    private boolean canAdd(int x, int y) {
        return Integer.MAX_VALUE - y < x ? false : true;
    }

    public static void main(String[] args) {
        ReverseInteger reverseInteger = new ReverseInteger();
        System.out.println(reverseInteger.reverse(1534236469));
    }
}
