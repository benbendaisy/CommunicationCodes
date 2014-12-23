package com.example.lee;

/**
 * Created by benbendaisy on 12/15/14.
 *
 * A peak element is an element that is greater than its neighbors.
 * Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
 * The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
 * You may imagine that num[-1] = num[n] = -∞.
 * For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
 */
public class FindPeakElement {
    public int findPeakElement(int[] num) {
        if(num == null){
            return -1;
        } else if (num.length == 1){
            return 0;
        } else {
            if(num[0] > num[1]){
                return 0;
            } else if (num[num.length-1] > num[num.length-2]){
                return num.length - 1;
            }
            for(int i = 1; i < num.length - 1; i++){
                if(num[i] > num[i-1] && num[i] > num[i+1]){
                    return i;
                }
            }
            return -1;
        }
    }
}
