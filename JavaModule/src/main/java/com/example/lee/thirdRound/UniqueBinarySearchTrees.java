package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

public class UniqueBinarySearchTrees {
    public int numTrees(int n) {
        if (n < 0) {
            return 0;
        }
        Map<Integer, Integer> cached = new HashMap<>();
        return numTreesHelper(n, cached);
    }
    private int numTreesHelper(int n, Map<Integer, Integer> cached) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if (cached.containsKey(n)) {
            return cached.get(n);
        }
        int count = 0;
        for (int i = 1; i <= n; i++) {
            int left = numTreesHelper(i - 1, cached);
            int right = numTreesHelper(n - i, cached);
            count += left * right;
        }
        cached.put(n, count);
        return count;
    }
}
