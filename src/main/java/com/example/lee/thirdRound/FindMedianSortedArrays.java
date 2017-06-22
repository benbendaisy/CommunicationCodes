package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 6/19/17.
 */
public class FindMedianSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if ((nums1 == null && nums2 == null) || (nums1.length == 0 && nums2.length == 0)) {
            return 0;
        } else if (nums1 == null || nums1.length == 0) {
            return nums2.length % 2 == 0 ? (nums2[nums2.length / 2 - 1] + nums2[nums2.length / 2])/2.0 : nums2[nums2.length / 2];
        } else if (nums2 == null || nums2.length == 0) {
            return nums1.length % 2 == 0 ? (nums1[nums1.length / 2 - 1] + nums1[nums1.length / 2])/2.0 : nums1[nums1.length / 2];
        }
        int len = nums1.length + nums2.length;
        if (len % 2 == 0) {
            double e1 = findTheKthElementOfSortedArrays(nums1, 0, nums1.length, nums2, 0, nums2.length, len / 2 + 1);
            double e2 = findTheKthElementOfSortedArrays(nums1, 0, nums1.length, nums2, 0, nums2.length, len / 2);
            return (e1 + e2) / 2.0;
        } else {
            return findTheKthElementOfSortedArrays(nums1, 0, nums1.length, nums2, 0, nums2.length, (len + 1) / 2);
        }
    }

    private double findTheKthElementOfSortedArrays(int[] nums1, int l1, int r1, int[] nums2, int l2, int r2, int k) {
        if (l1 > r1) {
            return nums2[l2 + k - 1];
        } else if (l2 > r2) {
            return nums1[l1 + k - 1];
        } else if (k == 1) {
            return Math.min(nums1[l1], nums2[l2]);
        }
        int len1 = r1 - l1;
        int len2 = r2 - l2;
        int m1 = (l1 + r1) / 2;
        int m2 = (l2 + r2) / 2;
        if (k > (len1 + len2) / 2 + 1) {
            int leftNumbers = k - (len1 + len2) / 2 - 1;
            if (nums1[m1] < nums2[m2]) {
                return findTheKthElementOfSortedArrays(nums1, m1 + 1, r1, nums2, l2, r2, k - len1 / 2 - 1);
            } else {
                return findTheKthElementOfSortedArrays(nums1, l1, r1, nums2, m2 + 1, r2, k - len2 / 2 - 1);
            }
        } else {
            if (nums1[m1] < nums2[m2]) {
                return findTheKthElementOfSortedArrays(nums1, l1, r1, nums2, l2, m2 - 1, k);
            } else {
                return findTheKthElementOfSortedArrays(nums1, l1, m1 - 1, nums2, l2, r2, k);
            }
        }
    }

    private double findTheKthElementOfSortedArraysI(int[] nums1, int l1, int r1, int[] nums2, int l2, int r2, int k) {
        if (l1 >= r1) {
            return nums2[l2 + k - 1];
        } else if (l2 >= r2) {
            return nums1[l1 + k - 1];
        } else if (k == 1) {
            return Math.min(nums1[l1], nums2[l2]);
        }
        int len1 = r1 - l1;
        int len2 = r2 - l2;
        int m1 = (l1 + r1) / 2;
        int m2 = (l2 + r2) / 2;
        if (nums1[m1] < nums2[m2]) {
            if (k > (len1 + len2)/2 + 1) {
                //remove left part in A and decrease the number that looking for
                return findTheKthElementOfSortedArraysI(nums1, m1 + 1, r1, nums2, l2, r2, k - m1/2 - 1);
            } else {
                //only remove right part in B
                return findTheKthElementOfSortedArraysI(nums1, l1, r1, nums2, l2, m2, k);
            }
        } else {
            if (k > (len1 + len2)/2 + 1) {
                //remove left part in B and decrease the number that looking for
                return findTheKthElementOfSortedArraysI(nums1, l1, r1, nums2, m2 + 1, r2, k - m2/2 - 1);
            } else {
                //only remove right part in A
                return findTheKthElementOfSortedArraysI(nums1, l1, m1, nums2, l2, r2, k);
            }
        }
    }

    public double findMedianSortedArraysII(int[] nums1, int[] nums2) {
        int total = nums1.length+nums2.length;
        if(total%2==0){
            return (findKth(total/2+1, nums1, nums2, 0, 0)+findKth(total/2, nums1, nums2, 0, 0))/2.0;
        }else{
            return findKth(total/2+1, nums1, nums2, 0, 0);
        }
    }

    private int findKth(int k, int[] nums1, int[] nums2, int s1, int s2){
        if(s1 >= nums1.length)
            return nums2[s2 + k-1];

        if(s2 >= nums2.length)
            return nums1[s1 + k-1];

        if(k == 1)
            return Math.min(nums1[s1], nums2[s2]);

        int m1 = s1 + k/2 - 1;
        int m2 = s2 + k/2 - 1;

        int mid1 = m1 < nums1.length ? nums1[m1] : Integer.MAX_VALUE;
        int mid2 = m2 < nums2.length ? nums2[m2] : Integer.MAX_VALUE;

        if(mid1 < mid2) {
            return findKth(k-k/2, nums1, nums2, m1+1, s2);
        } else {
            return findKth(k-k/2, nums1, nums2, s1, m2+1);
        }
    }

    /**
     * accepted by leetcode
     * referred to http://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/
     * @param nums1
     * @param nums2
     * @return
     */
    public double findMedianSortedArraysI(int[] nums1, int[] nums2) {
        if ((nums1 == null && nums2 == null) || (nums1.length == 0 && nums2.length == 0)) {
            return 0.0;
        } else if (nums1 == null || nums1.length == 0) {
            return nums2.length % 2 == 0 ? (nums2[nums2.length / 2 - 1] + nums2[nums2.length / 2]) / 2.0 : nums2[nums2.length / 2];
        } else if (nums2 == null || nums2 .length == 0) {
            return nums1.length % 2 == 0 ? (nums1[nums1.length / 2 - 1] + nums1[nums1.length / 2]) / 2.0 : nums1[nums1.length / 2];
        }
        int len = nums1.length + nums2.length;
        if (len % 2 == 0) {
            double m1 = findKthElement(nums1, nums2, 0, 0, len/2);
            double m2 = findKthElement(nums1, nums2, 0, 0, len/2 + 1);
            return (m1 + m2) / 2.0;
        } else {
            return findKthElement(nums1, nums2, 0, 0, len / 2);
        }
    }
    private double findKthElement(int[] nums1, int[] nums2, int s1, int s2, int k) {
        if (s1 >= nums1.length) {
            return nums2[s2 + k - 1];
        } else if (s2 >= nums2.length) {
            return nums1[s1 + k - 1];
        } else if (k == 1) {
            return Math.min(nums1[s1], nums2[s2]);
        }

        int m1 = s1 + k/2 - 1;
        int m2 = s2 + k/2 - 1;
        int mid1 = m1 < nums1.length ? nums1[m1] : Integer.MAX_VALUE;
        int mid2 = m2 < nums2.length ? nums2[m2] : Integer.MAX_VALUE;
        if (mid1 < mid2) {
            return findKthElement(nums1, nums2, m1 + 1, s2, k/2);
        } else {
            return findKthElement(nums1, nums2, s1, m2 + 1, k/2);
        }
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};
        FindMedianSortedArrays sortedArrays = new FindMedianSortedArrays();
        System.out.println(sortedArrays.findMedianSortedArraysI(nums1, nums2));
    }
}
