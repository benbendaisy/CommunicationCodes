package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Created by benbendaisy on 7/6/17.
 */
public class CombinationSumII {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        if (candidates == null || candidates.length < 1) {
            return Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        combinationSum2Helper(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    private void combinationSum2Helper(int[] candidates, int target, int idx, List<Integer> list, List<List<Integer>> res) {
        if (target == 0) {
            res.add(new ArrayList<>(list));
            return;
        }
        if (target < 0) {
            return;
        }
        int prev = -1;
        for (int i = idx; i < candidates.length; i++) {
            if (prev == candidates[i]) {
                continue;
            }
            list.add(candidates[i]);
            combinationSum2Helper(candidates, target - candidates[i], i + 1, list, res);
            list.remove(list.size() - 1);
            prev = candidates[i];
        }
    }

    public static void main(String[] args) {
        CombinationSumII combinationSumII = new CombinationSumII();
        int[] candidates = {10,1,2,7,6,1,5};
        combinationSumII.combinationSum2(candidates, 8).stream().forEach(System.out::println);
    }
}
