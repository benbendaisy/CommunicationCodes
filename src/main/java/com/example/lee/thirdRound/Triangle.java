package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Triangle {
    public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle == null || triangle.isEmpty()) {
            return 0;
        }
        int len = triangle.size();
        int[] dp = new int[len];
        for (int i = 0; i < len; i++) {
            dp[i] = triangle.get(len - 1).get(i);
        }
        for (int i = len - 2; i >= 0; i--) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                dp[j] = triangle.get(i).get(j) + Math.min(dp[j], dp[j + 1]);
            }
        }
        return dp[0];
    }

    public static void main(String[] args) {
        Triangle triangle = new Triangle();
        List<List<Integer>> lists = new ArrayList<>();
        lists.add(Arrays.asList(-1));
        lists.add(Arrays.asList(2, 3));
        lists.add(Arrays.asList(1, -1, -1));
        System.out.println(triangle.minimumTotal(lists));
    }
}
