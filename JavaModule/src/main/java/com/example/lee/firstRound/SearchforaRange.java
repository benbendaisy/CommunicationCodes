package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 2/26/15.
 */
public class SearchforaRange {
    public int[] searchRange(int[] A, int target) {
        int[] result = new int[2];
        if (null == A) {
            result[0] = -1;
            result[1] = -1;
            return result;
        }
        int left = 0, right = A.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (A[mid] == target) {
                int l = mid;
                while (l > 0 && A[l] == target) {
                    l--;
                }
                if (A[l] != target) {
                    l++;
                }

                int r = mid;
                while (r < A.length && A[r] == target) {
                    r++;
                }
                if (r == A.length || A[r] != target) {
                    r--;
                }

                result[0] = l;
                result[1] = r - 1;
                return result;
            } else if (A[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        result[0] = -1;
        result[1] = -1;
        return result;
    }

    public static void main(String[] args) {
        SearchforaRange searchforaRange = new SearchforaRange();
        int[] A = {1, 3};
        System.out.println(searchforaRange.searchRange(A, 1));
    }
}
