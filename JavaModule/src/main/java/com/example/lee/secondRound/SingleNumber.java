package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/4/15.
 */
public class SingleNumber {
    public int singleNumber(int[] A) {
        if (null == A) {
            return 0;
        }

        int res = A[0];
        for (int i = 1; i < A.length; i++) {
            res ^= A[i];
        }
        return res;
    }
}
