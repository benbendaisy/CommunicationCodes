package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 3/18/15.
 */
public class FindMinimuminRotatedSortedArrayII {
    public int findMin(int[] num) {
        if (null == num || num.length == 0) {
            return 0;
        } else if (num.length == 1) {
            return num[0];
        }
        int left = 0, right = num.length - 1;
        int min = Integer.MAX_VALUE;
        while (left <= right) {
            int mid = (left + right) / 2;
            min = Math.min(num[mid], min);
            if (num[left] < num[mid]) {
                min = Math.min(num[left], min);
                left = mid + 1;
            } else if (num[left] > num[mid]) {
                min = Math.min(num[right], min);
                right = mid - 1;
            } else {
                left++;
            }
        }
        return min;
    }
}
