package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 6/22/15.
 * <p>
 * Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
 * <p>
 * Each number in C may only be used once in the combination.
 * <p>
 * Note:
 * All numbers (including target) will be positive integers.
 * Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
 * The solution set must not contain duplicate combinations.
 * For example, given candidate set 10,1,2,7,6,1,5 and target 8,
 * A solution set is:
 * [1, 7]
 * [1, 2, 5]
 * [2, 6]
 * [1, 1, 6]
 */
public class CombinationSumII {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> lli = new ArrayList<>();
        if (null == candidates || candidates.length < 1 || target < 1) return lli;

        return null;
    }

    private void combSum(int[] candidates, int target, int idx, boolean[] res, int curSum, List<List<Integer>> lli) {
        if (idx == candidates.length || curSum < target) {
            return;
        } else if (target == curSum) {
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < res.length; i++) {
                if (res[i]) list.add(candidates[i]);
            }
            lli.add(list);
            return;
        }

        for (int i = idx; i < candidates.length; i++) {
            res[i] = true;
            combSum(candidates, target, idx + 1, res, candidates[i] + curSum, lli);
            res[i] = false;
        }
    }

}
