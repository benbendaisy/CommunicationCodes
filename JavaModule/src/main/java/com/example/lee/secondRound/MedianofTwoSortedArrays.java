package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/23/15.
 *
 * There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 *
 */
public class MedianofTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (null == nums1 && nums2 == null) return 0;
        if (null == nums1 || nums1.length == 0) return nums2.length % 2 == 0 ? (nums2[nums2.length / 2] + nums2[nums2.length/2 - 1]) / 2.0 : nums2[nums2.length / 2];
        if (null == nums2 || nums2.length == 0) return nums1.length % 2 == 0 ? (nums1[nums1.length / 2] + nums1[nums1.length/2 - 1]) / 2.0 : nums1[nums1.length / 2];
        int len = nums1.length + nums2.length;
        return len % 2 == 0 ? (findKthElement(nums1, nums2, 0, nums1.length - 1, 0, nums2.length -1, len / 2) + findKthElement(nums1, nums2, 0, nums1.length - 1, 0, nums2.length -1, len / 2 + 1)) / 2.0 : findKthElement(nums1, nums2, 0, nums1.length - 1, 0, nums2.length -1, (len + 1) / 2);
    }

    private double findKthElement(int[] nums1, int[] nums2, int idx1l, int idx1r, int idx2l, int idx2r, int k) {
        if (idx1l >= idx1r) {
            return nums2[idx2l + k - 1];
        } else if (idx2l >= idx2r) {
            return nums1[idx1l + k - 1];
        } else if (k == 1) {
            return Math.min(nums1[idx1l], nums2[idx2l]);
        }

        int lenA = idx1r - idx1l;
        int lenB = idx2r - idx2l;
        int ma = (idx1l + idx1r) / 2;
        int mb = (idx2l + idx2r) / 2;

        if (nums1[ma] < nums2[mb]) {
            return k > lenA / 2 + lenB / 2 + 1 ? findKthElement(nums1, nums2, ma + 1, idx1r, idx2l, idx2r, k - lenA/2 - 1) : findKthElement(nums1, nums2, idx1l, idx1r, idx2l, mb, k);
         } else {
            return k > lenA / 2 + lenB / 2 + 1 ? findKthElement(nums1, nums2, idx1l, idx1r, mb + 1, idx2r, k - lenB/2 - 1) : findKthElement(nums1, nums2, idx1l, ma, idx2l, idx2r, k);
        }

    }
}
