package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 4/29/15.
 *
 * Given a set of distinct integers, nums, return all possible subsets.
 *
 * Note:
 * Elements in a subset must be in non-descending order.
 * The solution set must not contain duplicate subsets.
 */
public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == nums || nums.length == 0) return lli;
        Arrays.sort(nums);
        lli.add(new ArrayList<Integer>());
        for (int i = 0; i < nums.length; i++) {
            List<List<Integer>> newLli = new ArrayList<List<Integer>>();
            for (List<Integer> li : lli) {
                List<Integer> list = new ArrayList<Integer>(li);
                list.add(nums[i]);
                newLli.add(list);
            }
            lli.addAll(newLli);
        }
        return lli;
    }
}
