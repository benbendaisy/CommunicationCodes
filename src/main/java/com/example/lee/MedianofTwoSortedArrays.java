package com.example.lee;

/**
 * Created by benbendaisy on 3/3/15.
 *
 * There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 */
public class MedianofTwoSortedArrays {

    //this iterative solution does not work but need a little change to fix it
    public double findMedianSortedArrays(int A[], int B[]) {
        if ((null == A && null == B) || (A.length == 0 && B.length == 0)) {
            return 0.0;
        } else if (null == A || A.length == 0) {
            return B.length % 2 == 0 ? (double)(B[B.length/2] + B[B.length/2 - 1])/2 : B[B.length/2];
        } else if (null == B || B.length == 0) {
            return A.length % 2 == 0 ? (double)(A[A.length/2] + A[A.length/2 - 1])/2 : A[A.length/2];
        }

        int la = 0, ra = A.length;
        int lb = 0, rb= B.length;
        int m = (ra + rb) / 2;
        boolean isEven = (A.length + B.length) % 2 == 0;
        while (la < ra && lb < rb) {
            if (m == 1) {
                return Math.min(A[la], B[lb]);
            }
            int ma = (la + ra) / 2;
            int mb = (lb + rb) / 2;
            int lena = ra - la;
            int lenb = rb - lb;
            if (A[ma] < B[mb]) {
                if (m > lena/2 + lenb/2 + 1) {
                    la = ma + 1;
                    m = m - lena/2 - 1;
                } else {
                    rb = mb;
                }
            } else {
                if (m > lena/2 + lenb/2 + 1) {
                    lb = mb + 1;
                    m = m - lenb/2 - 1;
                } else {
                    ra = ma;
                }
            }
        }

        if (la != ra && lb == rb) {
            if (isEven) {
                while (la < ra - 1) {
                    la++;
                    ra--;
                }
                return (double)(A[la] + A[ra]) / 2;
            } else {
                int ma = (la + ra + 1) / 2;
                return A[ma];
            }
        } else if (la == ra && lb != rb) {
            if (isEven) {
                while (lb < rb - 1) {
                    lb++;
                    rb--;
                }
                return (double)(B[lb] + B[rb]) / 2;
            } else {
                int mb = (lb + rb + 1) / 2;
                return B[mb];
            }
        } else {
            return (double) (Math.max(A[la], B[lb]) + Math.min(A[ra], B[rb]))/2;
        }
    }

    //refer to http://ackjack.com/leetcode-2-java-median-two-sorted-arrays/
    public double findMedianSortedArraysI(int A[], int B[]) {
        if ((null == A && null == B) || (A.length == 0 && B.length == 0)) {
            return 0.0;
        } else if (null == A || A.length == 0) {
            return B.length % 2 == 0 ? (B[B.length/2] + B[B.length/2 - 1])/2.0 : B[B.length/2];
        } else if (null == B || B.length == 0) {
            return A.length % 2 == 0 ? (A[A.length/2] + A[A.length/2 - 1])/2.0 : A[A.length/2];
        }
        int len = A.length + B.length;
        if (len % 2 == 0) {
            int m1 = findKSortedArrays(A, 0, A.length, B, 0, B.length, len/2);
            int m2 = findKSortedArrays(A, 0, A.length, B, 0, B.length, len/2 + 1);
            return (m1 + m2)/2.0;
        } else {
            return findKSortedArrays(A, 0, A.length, B, 0, B.length, (len + 1)/2);
        }
    }

    //find kth smallest number by recursive way
    private int findKSortedArrays(int A[], int la, int ra, int B[], int lb, int rb, int k) {
        if (la >= ra) {
            return B[lb + k - 1];
        } else if (lb >= rb) {
            return A[la + k - 1];
        } else if (k == 1) {
            return Math.min(A[la], B[lb]);
        }

        int lena = ra - la;
        int lenb = rb - lb;
        int ma = (la + ra)/2;
        int mb = (lb + rb)/2;
        if (A[ma] < B[mb]) {
            return k > lena/2 + lenb/2 + 1 ? findKSortedArrays(A, ma + 1, ra, B, lb, rb, k - lena/2 - 1) : findKSortedArrays(A, la, ra, B, lb, mb, k);
//            if (k > lena/2 + lenb/2 + 1) {
//                //remove left part in A and decrease the number that looking for
//                return findKSortedArrays(A, ma + 1, ra, B, lb, rb, k - lena/2 - 1);
//            } else {
//                //only remove right part in B
//                return findKSortedArrays(A, la, ra, B, lb, mb, k);
//            }
        } else {
            return k > lena/2 + lenb/2 + 1 ? findKSortedArrays(A, la, ra, B, mb + 1, rb, k - lenb/2 - 1) : findKSortedArrays(A, la, ma, B, lb, rb, k);
//            if (k > lena/2 + lenb/2 + 1) {
//                //remove left part in B and decrease the number that looking for
//                return findKSortedArrays(A, la, ra, B, mb + 1, rb, k - lenb/2 - 1);
//            } else {
//                //only remove right part in A
//                return findKSortedArrays(A, la, ma, B, lb, rb, k);
//            }
        }
    }

    private int getElement(int[] nums, int idx) {
        if (idx <= 0) {
            return nums[0];
        } else if (idx >= nums.length) {
            return nums[nums.length - 1];
        } else {
            return nums[idx];
        }
    }

    //use an iterative way to get median element
    public double findMedianSortedArraysII(int A[], int B[]) {
        if ((null == A && null == B) || (A.length == 0 && B.length == 0)) {
            return 0.0;
        } else if (null == A || A.length == 0) {
            return B.length % 2 == 0 ? (B[B.length/2] + B[B.length/2 - 1])/2.0 : B[B.length/2];
        } else if (null == B || B.length == 0) {
            return A.length % 2 == 0 ? (A[A.length/2] + A[A.length/2 - 1])/2.0 : A[A.length/2];
        }
        int len = A.length + B.length;
        if (len % 2 == 0) {
            double m1 = findKSortedArraysII(A, B, len/2);
            double m2 = findKSortedArraysII(A, B, len/2 + 1);
            return (m1 + m2)/2.0;
        } else {
            return findKSortedArraysII(A, B, (len + 1)/2);
        }
    }

    private double findKSortedArraysII(int[] A, int[] B, int m) {
        int la = 0, ra = A.length;
        int lb = 0, rb= B.length;
        while (la < ra && lb < rb) {
            // m <= 1 is also working
            if (m == 1) {
                return Math.min(A[la], B[lb]);
            }
            int ma = (la + ra) / 2;
            int mb = (lb + rb) / 2;
            int lena = ra - la;
            int lenb = rb - lb;
            if (A[ma] < B[mb]) {
                if (m > lena/2 + lenb/2 + 1) {
                    la = ma + 1;
                    m = m - lena/2 - 1;
                } else {
                    rb = mb;
                }
            } else {
                if (m > lena/2 + lenb/2 + 1) {
                    lb = mb + 1;
                    m = m - lenb/2 - 1;
                } else {
                    ra = ma;
                }
            }
        }

        if (la != ra && lb == rb) {
            return A[la + m - 1];
        } else if (la == ra && lb != rb) {
            return B[lb + m - 1];
        } else {
            return (Math.max(A[la], B[lb]) + Math.min(A[ra], B[rb]))/2.0;
        }
    }

    public static void main(String[] args) {
        MedianofTwoSortedArrays medianofTwoSortedArrays = new MedianofTwoSortedArrays();
        int[] A = {1, 1};
        int[] B = {1, 1};
        System.out.println(medianofTwoSortedArrays.findMedianSortedArrays(A, B));
    }
}
