package com.example.lee.thirdRound;

import java.util.Arrays;
import java.util.stream.Stream;

public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (nums1 == null || nums2 == null) {
            return;
        }
        int l1 = m - 1;
        int l2 = n - 1;
        int r = m + n - 1;
        while (l1 >= 0 && l2 >= 0) {
            if (nums1[l1] > nums2[l2]) {
                nums1[r] = nums1[l1];
                l1--;
            } else {
                nums1[r] = nums2[l2];
                l2--;
            }
            r--;
        }
        while (l2 >= 0) {
            nums1[r] = nums2[l2];
            r--;
            l2--;
        }
    }

    public static void main(String[] args) {
        MergeSortedArray mergeSortedArray = new MergeSortedArray();
        int[] nums1 = {2, 0};
        int[] nums2 = {1};
        mergeSortedArray.merge(nums1, 1, nums2, 1);
        Arrays.stream(nums1).forEach(System.out::println);
    }
}
