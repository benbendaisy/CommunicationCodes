package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by benbendaisy on 7/15/17.
 */
public class Combinations {
    public List<List<Integer>> combine(int n, int k) {
        if (k < 1) {
            return Collections.emptyList();
        }
        if (k > n) {
            k = n;
        }
        List<List<Integer>> res = new ArrayList<>();
        combineHelper(n, k, 1, new ArrayList<>(), res);
        return res;
    }

    private void combineHelper(int n, int k, int idx, List<Integer> candidates, List<List<Integer>> res) {
        if (candidates.size() == k) {
            res.add(new ArrayList<>(candidates));
            return;
        }
        for (int i = idx; i <= n; i++) {
            candidates.add(i);
            combineHelper(n, k, i + 1, candidates, res);
            candidates.remove(candidates.size() - 1);
        }
    }
}
