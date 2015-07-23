package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 6/22/15.
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
 *
 */
public class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> lli = new ArrayList<>();
        if (null == candidates || candidates.length < 1 || target < 1) return lli;
        Arrays.sort(candidates);
        comSum(candidates, target, candidates.length - 1, new ArrayList<>(), 0, lli);
        return lli;
    }

    private void comSum(int[] cands, int target, int idx, List<Integer> list, int curSum, List<List<Integer>> lli) {
        if (idx < 0 || curSum > target) {
            return;
        } else if (curSum == target) {
            lli.add(list);
            return;
        }
        for (int i = idx; i >= 0; i--) {
            List<Integer> newList = new ArrayList<>(list);
            newList.add(0, cands[i]);
            comSum(cands, target, idx, newList, curSum + cands[i], lli);
        }
    }
}
