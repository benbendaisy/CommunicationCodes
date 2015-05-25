package com.example.backtracking;

import java.util.Arrays;

/**
 * Created by benbendaisy on 5/22/15.
 */
public class SubsetSum {
    private void printSubset(int[] A, int idx) {
        for (int i = 0; i < idx; i++) System.out.print(A[i] + ", ");
        //for (int i : A) System.out.print(i + ", ");
        System.out.print("\n");
    }

    private void subSetSum(int[] s, int[] t, int tIdx, int sIdx, int sum, int target) {
        if (sum == target) {
            printSubset(t, tIdx);
            if (sIdx > 0 && sIdx < s.length && sum - s[sIdx - 1] + s[sIdx] <= target) {
                subSetSum(s, t, tIdx - 1, sIdx + 1, sum - s[sIdx], target);
            }
        } else {
            for (int i = sIdx; i < s.length; i++) {
                t[tIdx] = s[i];
                if (sum + s[i] <= target) subSetSum(s, t, tIdx + 1, i + 1, sum + s[i], target);
            }
        }
    }

    public void subSetSum(int[] s, int target) {
        if (null == s) return;
        Arrays.sort(s);
        int sum = 0;
        for (int i : s) sum += i;
        if (sum < target || s[0] > target) return;
        int[] t = new int[s.length];
        subSetSum(s, t, 0, 0, 0, target);
    }

    public static void main(String[] args) {
        SubsetSum subsetSum = new SubsetSum();
        int[] weights = {15, 22, 14, 26, 32, 9, 16, 8};
        int target = 53;
        subsetSum.subSetSum(weights, target);
    }
}
