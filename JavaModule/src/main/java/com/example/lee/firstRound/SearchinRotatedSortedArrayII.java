package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Follow up for "Search in Rotated Sorted Array":
 * What if duplicates are allowed?
 *
 * Would this affect the run-time complexity? How and why?
 *
 * Write a function to determine if a given target is in the array.
 */
public class SearchinRotatedSortedArrayII {
    public boolean search(int[] A, int target) {
        if(A == null || A.length == 0){
            return false;
        }
        int left = 0, right = A.length - 1;
        while(left <= right){
            int mid = (left + right)/2;
            if(A[mid] == target || A[left] == target || A[right] == target){
                return true;
            } else if(A[left] < target && A[mid] > target){
                right = mid - 1;
            } else if(A[right] > target && A[mid] < target){
                left = mid + 1;
            } else {
                //as there is duplicate, we can only discard one element in this scenario
                //can be right-- instead
                left++;
            }
        }
        return false;
    }
}
