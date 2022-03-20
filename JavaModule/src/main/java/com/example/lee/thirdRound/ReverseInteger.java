package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 6/22/17.
 */
public class ReverseInteger {
    public int reverse(int x) {
        if (x > -10 && x < 10) {
            return x;
        } else if (x == Integer.MIN_VALUE) {
            return 0;
        }

        boolean isNegative = x >= 0 ? false : true;
        if (isNegative) {
            x = -x;
        }
        int sum = 0;
        while (x > 0) {
            int remainer = x % 10;
            if (canMul(sum, 10) && canAdd(10 * sum, remainer)) {
                sum = 10 * sum + remainer;
            } else {
                return 0;
            }
            x = x / 10;
        }
        return isNegative ? -sum : sum;
    }

    private boolean canMul(int x, int y) {
        return Integer.MAX_VALUE / y >= x ? true : false;
    }

    private boolean canAdd(int x, int y) {
        return Integer.MAX_VALUE - y >= x ? true : false;
    }

    public static void main(String[] args) {
        ReverseInteger reverseInteger = new ReverseInteger();
        System.out.println(reverseInteger.reverse(-2147483412));
    }
}
