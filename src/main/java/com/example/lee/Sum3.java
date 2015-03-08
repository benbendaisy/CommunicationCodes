package com.example.lee;

import java.util.*;

/**
 * Created by benbendaisy on 3/2/15.
 *
 * Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
 *
 * Note:
 * Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
 * The solution set must not contain duplicate triplets.
 * For example, given array S = {-1 0 1 2 -1 -4},
 *
 * A solution set is:
 * (-1, 0, 1)
 * (-1, -1, 2)
 * Show Tags
 *
 */
public class Sum3 {
    public List<List<Integer>> threeSum(int[] num) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == num || num.length < 3) {
            return lli;
        }
        Set<List<Integer>> sli = new HashSet<List<Integer>>();
        Arrays.sort(num);
        for (int i = 0; i < num.length - 2; i++) {
            int l = i + 1, r = num.length - 1;
            int target = 0 - num[i];
            while (l < r) {
                if (num[l] + num[r] == target) {
                    List<Integer> li = new ArrayList<Integer>();
                    li.add(num[i]);
                    li.add(num[l]);
                    li.add(num[r]);
                    sli.add(li);
                    l++;
                    r--;
                } else if (num[l] + num[r] < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        lli.addAll(sli);
        return lli;
    }

    public List<List<Integer>> threeSumI(int[] num) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == num || num.length < 3) {
            return lli;
        }
        Set<List<Integer>> sli = new HashSet<List<Integer>>();
        Arrays.sort(num);
        for (int i = 0; i < num.length; i++) {
            int l = 0, r = num.length - 1;
            int target = 0 - num[i];
            while (l < r) {
                if (l == i) {
                    l++;
                } else if (r == i) {
                    r--;
                } else {
                    if (num[l] + num[r] == target) {
                        List<Integer> li = new ArrayList<Integer>();
                        if (i < l) {
                            li.add(num[i]);
                            li.add(num[l]);
                            li.add(num[r]);
                        } else if (i > r) {
                            li.add(num[l]);
                            li.add(num[r]);
                            li.add(num[i]);
                        } else {
                            li.add(num[l]);
                            li.add(num[i]);
                            li.add(num[r]);
                        }
                        sli.add(li);
                        l++;
                        r--;
                    } else if (num[l] + num[r] < target) {
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
}
