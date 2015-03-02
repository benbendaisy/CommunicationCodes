package com.example.lee;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 2/5/15.
 *
 * Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
 *
 * The same repeated number may be chosen from C unlimited number of times.
 *
 * Note:
 * All numbers (including target) will be positive integers.
 * Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
 * The solution set must not contain duplicate combinations.
 * For example, given candidate set 2,3,6,7 and target 7,
 * A solution set is:
 * [7]
 * [2, 2, 3]
 */
public class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> lists = new ArrayList<List<Integer>>();
        if(null == candidates || candidates.length == 0 || target < 0){
            return lists;
        }
        List<Integer> list = new ArrayList<Integer>();
        Arrays.sort(candidates);
        combinationSum(candidates, target, 0, list, lists);
        return lists;
    }

    public void combinationSum(int[] candidates, int target, int idx, List<Integer> list, List<List<Integer>> lists) {
        if(target == 0){
            lists.add(list);
        } else if(target < 0){
            return;
        }

        for(int i = idx; i < candidates.length; i++){
            List<Integer> newList = new ArrayList<>(list);
            newList.add(candidates[i]);
            combinationSum(candidates, target - candidates[i], i, newList, lists);
        }
    }
}
