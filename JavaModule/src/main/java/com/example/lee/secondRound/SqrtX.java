package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/12/15.
 */
public class SqrtX {
    public int mySqrt(int x) {
        if (x < 0) return -1;
        if (x == 0) return 0;
        long l = 0, r = x/2 + 1;
        while (l <= r) {
            long mid = (l + r) / 2;
            long p = mid * mid;
            if (p == x) {
                return (int) mid;
            } else if (p > x || p < 0) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return (int) r;
    }

    public static void main(String[] args) {
        SqrtX sqrtX = new SqrtX();
        System.out.println(sqrtX.mySqrt(2147395599));
    }
}
