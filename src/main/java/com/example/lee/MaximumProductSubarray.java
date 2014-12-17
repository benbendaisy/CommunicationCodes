package com.example.lee;

/**
 * Created by pzhong1 on 12/16/14.
 * Find the contiguous subarray within an array (containing at least one number) which has the largest product.
 * For example, given the array [2,3,-2,4],
 * the contiguous subarray [2,3] has the largest product = 6.
 */
public class MaximumProductSubarray {
    public int maxProduct(int[] A) {
        if(A == null){
            return -1;
        } else if( A.length == 1){
            return A[0];
        }
        long max = Integer.MIN_VALUE, localMax = 1;

        for(int i = 0; i < A.length; i++){
            if(A[i] != 0){
                localMax = localMax * A[i];
                if(max < localMax){
                    max = localMax;
                }
            } else {
                if(max < A[i]){
                    max = A[i];
                }
                localMax = 1;
            }
        }

        localMax = 1;
        for(int i = A.length -1; i > 0; i--){
            if(A[i] != 0){
                localMax = localMax * A[i];
                if(max < localMax){
                    max = localMax;
                }
            } else {
                localMax = 1;
            }
        }

        return max > Integer.MAX_VALUE ? Integer.MAX_VALUE : (int) max;
    }
}
