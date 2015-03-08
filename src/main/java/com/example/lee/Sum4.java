package com.example.lee;

import java.util.*;

/**
 * Created by benbendaisy on 3/2/15.
 *
 * Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
 *
 * Note:
 * Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
 * The solution set must not contain duplicate quadruplets.
 * For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
 *
 * A solution set is:
 * (-1,  0, 0, 1)
 * (-2, -1, 1, 2)
 * (-2,  0, 0, 2)
 */
public class Sum4 {
    public List<List<Integer>> fourSum(int[] num, int target) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == num || num.length < 4) {
            return lli;
        }
        Set<List<Integer>> sli = new HashSet<List<Integer>>();
        Arrays.sort(num);
        for (int left = 0; left < num.length - 3; left++) {
            for (int right = num.length - 1; right > left; right--) {
                int l = left + 1, r = right - 1;
                int newTarget = target - num[left] - num[right];
                while (l < r) {
                    int sum2 = num[l] + num[r];
                    if ( sum2 == newTarget) {
                        List<Integer> li = new ArrayList<Integer>();
                        li.add(num[left]);
                        li.add(num[l]);
                        li.add(num[r]);
                        li.add(num[right]);
                        sli.add(li);
                        l++;
                        r--;
                    } else if (sum2 < newTarget) {
                        l++;
                    } else {
                        r--;
                    }
                }
            }
        }

        lli.addAll(sli);
        return lli;
    }

    public static void main(String[] args) {
        Sum4 sum4 = new Sum4();
        int[] num = {0, 0, 0, 0};
        System.out.println(sum4.fourSum(num, 0));
    }
}
