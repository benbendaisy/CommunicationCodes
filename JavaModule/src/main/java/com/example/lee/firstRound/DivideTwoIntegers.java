package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 2/26/15.
 * Divide two integers without using multiplication, division and mod operator.
 *
 * If it is overflow, return MAX_INT.
 */
public class DivideTwoIntegers {

    /*
     * a number can be divided as num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n
     * refer to http://blog.csdn.net/linhuanmars/article/details/20024907
     */
    public int divide(int dividend, int divisor) {
        if (divisor == 0) {
            return Integer.MAX_VALUE;
        } else if (divisor == 1) {
            return dividend;
        }

        boolean isNegative = (dividend ^ divisor) >>> 31 == 1;
        int result = 0;
        if (dividend == Integer.MIN_VALUE) {
            dividend += Math.abs(divisor);
            if (divisor == -1) {
                return Integer.MAX_VALUE;
            }
            result++;
        }

        if (divisor == Integer.MIN_VALUE) {
            return result;
        }

        dividend = Math.abs(dividend);
        divisor = Math.abs(divisor);

        //find the minimal moves that make divisor less than dividend
        int it = 0;
        while (divisor <= (dividend >> 1)) {
            divisor <<= 1;
            it++;
        }


        while (it >= 0) {
            while (dividend >= divisor) {
                dividend -= divisor;
                result += 1 << it;
            }
            divisor = divisor >> 1;
            it--;
        }

        return isNegative ? -result : result;
    }

    public static void main(String[] args) {
        DivideTwoIntegers divideTwoIntegers = new DivideTwoIntegers();
        System.out.println(divideTwoIntegers.divide(-8, 2));
        StringBuilder sb = new StringBuilder();
    }
}
