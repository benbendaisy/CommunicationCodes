package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 2/26/15.
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 *
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 *
 * You are given a target value to search. If found in the array return its index, otherwise return -1.
 *
 * You may assume no duplicate exists in the array.
 */
public class SearchinRotatedSortedArray {
    public int search(int[] A, int target) {
        if (null == A || A.length == 0) {
            return -1;
        }
        int left = 0, right = A.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (A[mid] == target) {
                return mid;
            } else if (A[mid] < target && A[left] < A[right]) {
                left = mid + 1;
            } else if (A[mid] > target && A[left] < A[right]) {
                right = mid - 1;
            } else {
                if (A[left] == target) {
                    return left;
                } else if (A[right] == target) {
                    return right;
                }
                left++;
            }
        }
        return -1;
    }
}
