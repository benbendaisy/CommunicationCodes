package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 12/11/14.
 * Find Minimum in Rotated Sorted Array
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * Find the minimum element.
 * You may assume no duplicate exists in the array.
 */
public class MinRotatedSortedArray {
    public int findMin(int[] num) {
        if(null == num){
            return -1;
        } else if(num.length == 1){
            return num[0];
        }
        int left = 0, right = num.length - 1;
        int min = Integer.MAX_VALUE;
        while(left <= right){
            int mid = (left + right) / 2;
            if(num[mid] < min ){
                min = num[mid];
            }
            if(num[left] < num[mid]){
                min = Math.min(min, num[left]);
                left = mid + 1;
            } else {
                min = Math.min(min, num[right]);
                right = mid -1;
            }
        }
        return min;
    }
}
