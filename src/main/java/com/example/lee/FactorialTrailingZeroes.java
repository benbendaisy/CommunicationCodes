package com.example.lee;

/**
 * Created by benbendaisy on 12/29/14.
 * Given an integer n, return the number of trailing zeroes in n!.
 * Note: Your solution should be in logarithmic time complexity.
 * please refer to https://oj.leetcode.com/discuss/19844/o-log_5-n-solution-java
 * only need to count the number of 5 in n!
 */
public class FactorialTrailingZeroes {
    public int trailingZeroes(int n) {
        if(n <= 0){
            return 0;
        }
        int count5 = 0;

        while(n >= 5){
            n = n/5;
            count5 += n;
        }
        return count5;
    }
}
