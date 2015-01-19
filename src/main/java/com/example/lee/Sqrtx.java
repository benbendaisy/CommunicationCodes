package com.example.lee;

/**
 * Created by pzhong1 on 1/18/15.
 *
 * Implement int sqrt(int x).
 *
 * Compute and return the square root of x.
 */
public class Sqrtx {
    public int sqrt(int x) {
        if(x <= 0){
            return 0;
        }
        long left = 0, right = x/2 + 1;
        while(left <= right){
            long mid = (left + right)/2;
            long y = mid * mid;
            if(y == x){
                return (int)mid;
            } else if(y < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return (int)right;
    }

    public static void main(String[] args) {
        Sqrtx sqrtx = new Sqrtx();
        System.out.println(sqrtx.sqrt(2147483647));
    }
}
