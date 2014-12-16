package com.example.lee;

/**
 * Created by pzhong1 on 12/15/14.
 * Follow up for "Find Minimum in Rotated Sorted Array":
 * What if duplicates are allowed?
 * Would this affect the run-time complexity? How and why?
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * Find the minimum element.
 * The array may contain duplicates.
 */
public class MinRotatedSortedArrayII {
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
            } else if(num[left] > num[mid]) {
                min = Math.min(min, num[right]);
                right = mid -1;
            } else {
                left++;
            }
        }
        return min;
    }
//    public int findMin(int[] num) {
//        if(null == num){
//            return -1;
//        } else if(num.length == 1){
//            return num[0];
//        }
//        int left = 0, right = num.length - 1;
//        return findMinHelp(num, 0, num.length - 1, Integer.MAX_VALUE);
//    }
//    private int findMinHelp(int[] num, int left, int right, int min){
//        if(left > right){
//            return min;
//        }
//        int mid = (left + right) / 2;
//        if(min > num[mid]){
//            min = num[mid];
//        }
//        if(num[left] < num[mid]){
//            if(num[mid] > num[right]){
//                min = findMinHelp(num, left + 1, right, min);
//            } else {
//                min = findMinHelp(num, left, right - 1, min);
//            }
//        } else if (num[left] > num[mid]) {
//            min = findMinHelp(num, left, right - 1, min);
//        } else {
//            int l = findMinHelp(num, left + 1, right, min);
//            int r = findMinHelp(num, left, right - 1, min);
//            min = l < r ? l : r;
//        }
//        return min;
//    }
}
