package com.example.lee.firstRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 2/5/15.
 *
 * Given an unsorted integer array, find the first missing positive integer.
 *
 * For example,
 * Given [1,2,0] return 3,
 * and [3,4,-1,1] return 2.
 * refers to http://blog.csdn.net/kenden23/article/details/17099987
 */
public class FirstMissingPositive {

    //put the number to the number - 1 of A
    public int firstMissingPositive(int[] A) {
        if(null == A || A.length == 0){
            return 1;
        }

        for(int i = 0; i < A.length; i++){
            while(A[i] <= A.length && A[i] > 0 && A[A[i] - 1] != A[i]){
                swap(A, A[i] - 1, i);
            }
        }

        for(int i = 0; i < A.length; i++){
            if(i + 1 != A[i]){
                return i + 1;
            }
        }

        return A.length + 1;
    }

    private void swap(int[] A, int i, int j){
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }

    //sort and choose the right element
    public int firstMissingPositiveI(int[] A) {
        if (null == A || A.length == 0) {
            return 1;
        }
        Arrays.sort(A);
        int res = 0;
        int i = 0;
        //remove 0 or negative numbers
        while (i < A.length && A[i] <= 0) i++;
        for (; i < A.length; i++)
        {
            //pass duplicate
            if (i>0 && A[i] == A[i-1]) {
                continue;
            }

            //find the right element
            if (A[i] - res != 1) {
                return res+1;
            } else {
                res = A[i];
            }
        }
        return res+1;
    }

    //The only difference with the first method is to consider 0
    public int firstMissingPositiveII(int[] A) {
        if(null == A || A.length == 0){
            return 1;
        }

        for(int i = 0; i < A.length; i++){
            while(A[i] < A.length && A[i] >= 0 && A[A[i]] != A[i]){
                swap(A, A[i], i);
            }
        }

        for(int i = 0; i < A.length; i++){
            if(i != A[i]){
                return i;
            }
        }

        return A[0] == A.length ? A.length + 1 : A.length;
    }
}
