package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/10/15.
 */
public class Combinations {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (n <= 0 || k <= 0) return lli;
        if (k > n) k = n;
        List<Integer> li = new ArrayList<Integer>();
        combine(n, k, 1, lli, li);
        return lli;
    }

    private void combine(int n, int k, int idx, List<List<Integer>> lli, List<Integer> li) {
        if (li.size() == k) {
            lli.add(li);
            return;
        } else if (idx > n || n - idx + 1 + li.size() < k) {
            return;
        }
        for (int i = idx; i <= n; i++) {
            List<Integer> newLi = new ArrayList<Integer>(li);
            newLi.add(i);
            combine(n, k, i + 1, lli, newLi);
        }
    }
}
