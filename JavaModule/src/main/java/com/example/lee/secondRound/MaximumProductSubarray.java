package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 3/19/15.
 */
public class MaximumProductSubarray {
    public int maxProduct(int[] A) {
        if (null == A || A.length < 1) {
            return 0;
        } else if (A.length == 1) {
            return A[0];
        }
        int[] lPro = new int[A.length];
        int[] rPro = new int[A.length];
        lPro[0] = A[0];
        for (int i = 1; i < A.length; i++) {
            if (lPro[i - 1] == 0) {
                lPro[i] = A[i];
            } else {
                lPro[i] = A[i] * lPro[i - 1];
            }
        }
        rPro[A.length - 1] = A[A.length - 1];
        for (int i = A.length - 2; i >= 0; i--) {
            if (rPro[i + 1] == 0) {
                rPro[i] = A[i];
            } else {
                rPro[i] = A[i] * rPro[i + 1];
            }
        }

        int max = Integer.MIN_VALUE;
        for (int i = 0; i < A.length; i++) {
            max = Math.max(max, lPro[i]);
            max = Math.max(max, rPro[i]);
        }
        return max;
    }
}
