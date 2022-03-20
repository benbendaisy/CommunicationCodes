package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/30/15.
 *
 * Given two sorted integer arrays A and B, merge B into A as one sorted array.
 *
 * Note:
 * You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
 */
public class MergeSortedArray {
    public void merge(int A[], int m, int B[], int n) {
        if (null == A || null == B || A.length + B.length < m + n || B.length == 0) return;
        int r = m + n - 1;
        m--; n--;
        while (r > m && m >= 0 && n >= 0) {
            if (A[m] > B[n]) {
                A[r] = A[m];
                m--;
            } else {
                A[r] = B[n];
                n--;
            }
            r--;
        }
        while (n >= 0) {
            A[r] = B[n];
            r--;
            n--;
        }
    }
}
