package com.example.lee.thirdRound;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Created by benbendaisy on 7/6/17.
 */
public class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if (candidates == null || candidates.length < 1) {
            return Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();
        combinationSumHelper(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    private void combinationSumHelper(int[] candidates, int target, int idx, List<Integer> list, List<List<Integer>> res) {
        if (target == 0) {
            res.add(new ArrayList<>(list));
            return;
        }

        if (target < 0) {
            return;
        }

        for (int i = idx; i < candidates.length; i++) {
            list.add(candidates[i]);
            combinationSumHelper(candidates, target - candidates[i], i, list, res);
            list.remove(list.size() - 1);
        }
    }

    public static void main(String[] args) {
        CombinationSum combinationSum = new CombinationSum();
        int[] candidates = {1, 2};
        combinationSum.combinationSum(candidates, 4).stream().forEach(System.out::println);
    }

}
