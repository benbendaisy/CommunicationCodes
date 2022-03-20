package com.example.lee.firstRound;

/**
 * Created by pzhong1 on 1/18/15.
 *
 * You are climbing a stair case. It takes n steps to reach to the top.
 *
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 */
public class ClimbingStairs {
    public int climbStairs(int n) {
        if(n == 0){
            return 0;
        } else if(n == 1){
            return 1;
        } else if(n == 2){
            return 2;
        }

        int first = 1, second = 2;
        int current = 0, index = 3;
        while(index <= n){
            current = first + second;
            first = second;
            second = current;
            index++;
        }
        return current;
    }
}
