package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/10/15.
 *
 * Given two sorted integer arrays A and B, merge B into A as one sorted array.
 *
 * Note:
 * You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
 */
public class MergeSortedArray {
    public void merge(int A[], int m, int B[], int n) {
        if(A == null || B == null || B.length == 0){
            return;
        }
        for(int i = m - 1; i >= 0; i--){
            A[n + i] = A[i];
        }

        int leftA = 0, leftB = 0;
        while(leftA < m && leftB < n){
            if(A[n + leftA] < B[leftB]){
                A[leftA + leftB] = A[n + leftA];
                leftA++;
            } else {
                A[leftA + leftB] = B[leftB];
                leftB++;
            }
        }

        while(leftB < n){
            A[leftA + leftB] = B[leftB];
            leftB++;
        }
    }
}
