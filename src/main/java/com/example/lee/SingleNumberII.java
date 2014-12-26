package com.example.lee;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 12/23/14.
 * Given an array of integers, every element appears three times except for one. Find that single one.
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 */
public class SingleNumberII {

    //using hashmap, time complexity O(n), space complexity O(n);
    public int singleNumber(int[] A) {
        if(A == null || A.length < 1){
            return -1;
        } else if(A.length == 1){
            return A[0];
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i : A){
            if(map.containsKey(i)){
                map.put(i, map.get(i) + 1);
            } else {
                map.put(i, 1);
            }
        }

        for(int key : map.keySet()){
            if(map.get(key) != 3){
                return key;
            }
        }

        return -1;
    }

    //using bit operations, time complexity O(n), space complexity O(1);
    //basic idea is to get each bit of result
    //here mod 3 is that number appears 3 times
    //pleas refer to https://oj.leetcode.com/discuss/857/constant-space-solution
    public int singleNumberI(int[] A) {
        if(A == null || A.length < 1|| A.length == 2){
            return -1;
        } else if(A.length == 1){
            return A[0];
        }
        int[] count = new int[32];
        int result = 0;
        int len = A.length;
        for (int i = 0; i < 32; i++) {
            for (int j = 0; j < len; j++) {
                if (((A[j] >> i) & 1) != 0) {
                    count[i]++;
                }
            }
            result |= ((count[i] % 3) << i);
        }
        return result;
    }

    //a better bit solution but harder to understand
    /*
    * We can improve this based on the previous solution using three bitmask variables:
    * ones as a bitmask to represent the ith bit had appeared once.
    * twos as a bitmask to represent the ith bit had appeared twice.
    * threes as a bitmask to represent the ith bit had appeared three times.
    * When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0. The final answer will be the value of ones.
    */
    int singleNumberII(int A[]) {
        if(A == null || A.length < 1 || A.length == 2){
            return -1;
        } else if(A.length == 1){
            return A[0];
        }
        int ones = 0, twos = 0, threes = 0;
        int len = A.length;
        for (int i = 0; i < len; i++) {
            twos |= ones & A[i];
            ones ^= A[i];
            threes = ones & twos;
            ones &= ~threes;
            twos &= ~threes;
        }
        return ones;
    }

    public static void main(String[] args) {
        int[] A = {2, 3, 3, 3};
        SingleNumberII singleNumber = new SingleNumberII();
        System.out.println(singleNumber.singleNumberII(A));
    }
}
