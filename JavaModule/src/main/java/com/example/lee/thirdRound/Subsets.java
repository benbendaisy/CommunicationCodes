package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by benbendaisy on 7/15/17.
 */
public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        if (nums == null || nums.length < 1) {
            return Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        for (int i = 0; i < nums.length; i++) {
            List<List<Integer>> newLists = new ArrayList<>();
            for (List<Integer> list : res) {
                List<Integer> newList = new ArrayList<>(list);
                newList.add(nums[i]);
                newLists.add(newList);
            }
            res.addAll(newLists);
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        Subsets subsets = new Subsets();
        subsets.subsets(nums).stream().forEach(System.out::println);
    }
}
