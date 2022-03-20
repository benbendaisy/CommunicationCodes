package com.example.lee.thirdRound;

import java.util.*;

public class SubsetsII {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        if (nums == null || nums.length < 1) {
            return Collections.emptyList();
        }
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();
        res.add(new ArrayList<>());
        for (int num : nums) {
            Set<List<Integer>> tempSet = new HashSet<>();
            for (List<Integer> list : res) {
                List<Integer> newList = new ArrayList<>(list);
                newList.add(num);
                tempSet.add(newList);
            }
            res.addAll(tempSet);
        }
        return new ArrayList<>(res);
    }
}
