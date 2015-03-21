package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 3/18/15.
 */
public class FindMinimuminRotatedSortedArray {
    public int findMin(int[] num) {
        if (null == num || num.length == 0) {
            return 0;
        } else if (num.length == 1) {
            return num[0];
        }

        int left = 0, right = num.length - 1;
        int mid = 0, min = Integer.MAX_VALUE;
        while (left <= right) {
            mid = (left + right) / 2;
            min = Math.min(min, num[mid]);
            if (num[left] < num[mid]) {
                min = Math.min(min, num[left]);
                left = mid + 1;
            } else {
                min = Math.min(min, num[right]);
                right = mid - 1;
            }
        }
        return min;
    }
}
