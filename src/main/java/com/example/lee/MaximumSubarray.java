package com.example.lee;

/**
 * Created by benbendaisy on 1/27/15.
 *
 * Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
 *
 * For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
 * the contiguous subarray [4,−1,2,1] has the largest sum = 6.
 */
public class MaximumSubarray {
    public int maxSubArray(int[] A) {
        if(A == null || A.length < 1){
            return 0;
        }
        int max = Integer.MIN_VALUE;
        int localMax = 0;
        for(int i = 0; i < A.length; i++){
            localMax += A[i];
            max = Math.max(max, localMax);
            if(localMax <= 0){
                localMax = 0;
            }
        }
        return max;
    }
}
