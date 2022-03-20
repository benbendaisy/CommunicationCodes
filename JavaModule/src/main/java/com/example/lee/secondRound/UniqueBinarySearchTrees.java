package com.example.lee.secondRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/19/15.
 *
 * Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
 *
 * For example,
 * Given n = 3, there are a total of 5 unique BST's.
 *
 * 1         3     3      2      1
 * \       /     /      / \      \
 * 3     2     1      1   3      2
 * /     /       \                 \
 * 2     1         2                 3
 */
public class UniqueBinarySearchTrees {
    //by recursive way with memoization
    public int numTrees(int n) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        return numTrees(n, map);
    }

    private int numTrees(int n, Map<Integer, Integer> map) {
        if (n <= 1) {
            return 1;
        } else if (map.containsKey(n)) {
            return map.get(n);
        }
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            int left = numTrees(i - 1, map);
            int right = numTrees(n - i, map);
            cnt += left * right;
        }
        map.put(n, cnt);
        return cnt;
    }

    //by dp
    public int numTreesI(int n) {
        if (n < 0) {
            return 0;
        } else if (n < 2) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }
        return dp[n];
    }
}
