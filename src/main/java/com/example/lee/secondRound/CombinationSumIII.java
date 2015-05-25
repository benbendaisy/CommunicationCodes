package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/24/15.
 *
 * Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
 *
 * Ensure that numbers within the set are sorted in ascending order.
 *
 * Example 1:
 *
 * Input: k = 3, n = 7
 *
 * Output:
 *
 * [[1,2,4]]
 *
 * Example 2:
 *
 * Input: k = 3, n = 9
 *
 * Output:
 *
 * [[1,2,6], [1,3,5], [2,3,4]]
 *
 */
public class CombinationSumIII {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (k < 1) return lli;
        boolean[] cands = new boolean[9];
        combinationSum3(k, n, 1, 0, lli, cands);
        return lli;
    }

    private void combinationSum3(int k, int target, int idx, int sum, List<List<Integer>> lli, boolean[] cands){
        if (k == 0 && sum == target) {
            List<Integer> li = new ArrayList<Integer>();
            for (int i = 0; i < cands.length; i++) {
                if (cands[i]) li.add(i + 1);
            }
            lli.add(li);
            return;
        } else if (k == 0 || idx > 9) {
            return;
        }

        for (int i = idx; i <= 9; i++) {
            cands[i - 1] = true;
            combinationSum3(k - 1, target, i + 1, sum + i, lli, cands);
            cands[i - 1] = false;
        }
    }
}
