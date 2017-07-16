package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/13/17.
 */
public class SqrtX {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int r = x / 2 + 1;
        int l = 0;
        while (l <= r) {
            int m = (l + r) / 2;
            if (m == x / m) {
                return m;
            } else if (m < x / m) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return r;
    }

    public static void main(String[] args) {
        SqrtX sqrtX = new SqrtX();
        System.out.println(sqrtX.mySqrt(2));
        System.out.println(sqrtX.mySqrt(3));
        System.out.println(sqrtX.mySqrt(5));
        System.out.println(sqrtX.mySqrt(6));
        System.out.println(sqrtX.mySqrt(7));
        System.out.println(sqrtX.mySqrt(9));
        System.out.println(sqrtX.mySqrt(10));
    }
}
