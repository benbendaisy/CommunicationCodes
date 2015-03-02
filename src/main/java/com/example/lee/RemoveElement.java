package com.example.lee;

/**
 * Created by benbendaisy on 2/26/15.
 *
 * Given an array and a value, remove all instances of that value in place and return the new length.
 *
 * The order of elements can be changed. It doesn't matter what you leave beyond the new length.
 */
public class RemoveElement {
    public int removeElement(int[] A, int elem) {
        if (null == A || A.length == 0) {
            return 0;
        }
        int left = 0, right = A.length - 1;
        int len = A.length;
        while (left < right) {
            while (right > left && A[left] == elem) {
                swap(A, left, right);
                len--;
                right--;
            }
            if (left < right) {
                left++;
            }
        }
        if (A[left] == elem) {
            len--;
        }
        return len;
    }

    private void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
}
