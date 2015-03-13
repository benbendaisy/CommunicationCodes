package com.example.lee.firstRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 12/23/14.
 * Given an array of integers, every element appears twice except for one. Find that single one.
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 */
public class SingleNumber {

    public int singleNumberI(int[] A) {
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
            if(map.get(key) != 2){
                return key;
            }
        }

        return -1;
    }

    public int singleNumber(int[] A) {

        if(A == null || A.length < 1){
            return -1;
        } else if(A.length == 1){
            return A[0];
        }

        int temp = 0;
        for(int i = 0; i < A.length; i++){
            temp = temp^A[i];
        }

        return temp;
    }

    public static void main(String[] args) {
        SingleNumber singleNumber = new SingleNumber();
        int[] A = {2, 2, 1};
        System.out.println(singleNumber.singleNumber(A));
    }
}
