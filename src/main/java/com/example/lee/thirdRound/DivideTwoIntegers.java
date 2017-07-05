package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/3/17.
 */
public class DivideTwoIntegers {

    /**
     * http://www.programcreek.com/2014/05/leetcode-divide-two-integers-java/
     * This problem can be solved based on the fact that any number can be converted to the format of the following:
     *
     * num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n
     * The time complexity is O(logn).
     *
     * @param dividend
     * @param divisor
     * @return
     */
    public int divide(int dividend, int divisor) {
        if (divisor == 0) {
            return Integer.MAX_VALUE;
        } else if (divisor == 1) {
            return dividend;
        } else if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean isNeg = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0) ? false : true;
        long pDividend = Math.abs((long) dividend);
        long pDivisor = Math.abs((long) divisor);
        int res = 0;
        while (pDividend >= pDivisor) {
            int leftShift = 0;
            while (pDividend >= (pDivisor << leftShift)) {
                leftShift++;
            }
            res += 1 << (leftShift -1);
            pDividend -= (pDivisor << (leftShift - 1));
        }
        return isNeg ? -res : res;
    }

    /**
     * naive solution by minus but not pass leetcode because of time limit exceeded
     * @param dividend
     * @param divisor
     * @return
     */
    public int divideI(int dividend, int divisor) {
        if (dividend == 0) {
            return 0;
        } else if (divisor == 1) {
            return dividend;
        }
        boolean isNeg = false;
        if (dividend < 0) {
            isNeg = true;
            dividend = dividend == Integer.MIN_VALUE ? Integer.MAX_VALUE : -dividend;
        }
        if (divisor < 0) {
            isNeg = !isNeg;
            divisor = -divisor;
        }
        if (divisor == 1) {
            return isNeg ? -dividend : dividend;
        }
        int result = 0;
        while (dividend >= divisor) {
            dividend = dividend - divisor;
            result++;
        }
        return isNeg ? -result : result;
    }

    public static void main(String[] args) {
        DivideTwoIntegers divideTwoIntegers = new DivideTwoIntegers();
        System.out.println(divideTwoIntegers.divide(-2147483648,-1));
    }
}
