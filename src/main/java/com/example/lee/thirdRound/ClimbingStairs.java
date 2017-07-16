package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 7/14/17.
 */
public class ClimbingStairs {
    /**
     * both solutions passed leetcode
     * @param n
     * @return
     */
    public int climbStairs(int n) {
        if (n < 2) {
            return 1;
        }
        Map<Integer, Integer> cache = new HashMap<>();
        return climbStairsHelper(n, cache);
    }

    private int climbStairsHelper(int n, Map<Integer, Integer> cache) {
        if (cache.containsKey(n)) {
            return cache.get(n);
        }
        if (n == 0 || n == 1) {
            cache.put(n, 1);
            return 1;
        }

        int res = climbStairsHelper(n - 1, cache) + climbStairsHelper(n - 2, cache);
        cache.put(n, res);
        return res;
    }

    public int climbStairsI(int n) {
        if (n < 2) {
            return 1;
        }

        int n_1 = 1, n_2 = 1;
        int res = 0;
        int i = 1;
        while (i < n) {
            res = n_1 + n_2;
            n_2 = n_1;
            n_1 = res;
            i++;
        }
        return res;
    }
}
