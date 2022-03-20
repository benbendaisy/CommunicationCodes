package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/22/15.
 */
public class DivideTwoIntegers {
    public int divide(int dividend, int divisor) {
        if (divisor == 0) {
            return Integer.MAX_VALUE;
        } else if (divisor == 1) {
            return dividend;
        }
        boolean isNegative = (dividend ^ divisor) >>> 31 == 1;

        int res = 0;
        if (dividend == Integer.MIN_VALUE) {
            dividend += Math.abs(divisor);
            if (divisor == -1) return Integer.MAX_VALUE;
            res++;
        }
        if (divisor == Integer.MIN_VALUE) return res;
        int it = 0;
        dividend = Math.abs(dividend);
        divisor = Math.abs(divisor);
        while (divisor <= (dividend >> 1)) {
            divisor <<= 1;
            it++;
        }

        while (it >= 0) {
            while (dividend >= divisor) {
                dividend -= divisor;
                res += 1 << it;
            }
            divisor >>= 1;
            it--;
        }

        return isNegative ? -res : res;
    }
}
