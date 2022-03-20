package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 5/31/15.
 */
public class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == nums || nums.length < 1) return lli;
        permute(nums, lli, 0);
        return lli;
    }

    private void permute(int[] nums, List<List<Integer>> lli, int idx){
        if (idx == nums.length) {
            List<Integer> list = new ArrayList<Integer>();
            for (int i : nums) list.add(i);
            lli.add(list);
            return;
        }
        for (int i = idx; i < nums.length; i++) {
            swap(nums, i, idx);
            permute(nums, lli, idx + 1);
            swap(nums, i, idx);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
}
