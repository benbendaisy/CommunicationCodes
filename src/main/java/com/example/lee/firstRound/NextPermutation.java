package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 2/26/15.
 * Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
 *
 * If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
 *
 * The replacement must be in-place, do not allocate extra memory.
 *
 * Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 */
public class NextPermutation {
    public void nextPermutation(int[] num) {

        if (null == num || num.length <= 1) {
            return;
        }
        int idx = num.length - 1;
        while (idx > 0 && num[idx] <= num[idx - 1]) {
            idx--;
        }

        //do not find right candidate. sort
        if (idx == 0) {
            int left = 0, right = num.length - 1;
            while (left < right) {
                swap(num, left, right);
                left++;
                right--;
            }
            return;
        }

        //find right candidate
        int r = num.length - 1;
        while (r >= idx && num[idx -1] >= num[r]) {
            r--;
        }
        swap(num, r, idx - 1);

        //reverse right part
        int left = idx, right = num.length - 1;
        while (left < right) {
            swap(num, left, right);
            left++;
            right--;
        }
    }

    private void swap(int[] num, int i, int j) {
        int temp = num[i];
        num[i] = num[j];
        num[j] = temp;
    }
}
