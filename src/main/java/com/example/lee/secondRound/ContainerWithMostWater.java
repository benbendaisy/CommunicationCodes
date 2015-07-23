package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/23/15.
 *
 * Given n non-negative integers a1, a2, ..., an, where each represents a
 * point at coordinate (i, ai). n vertical lines are drawn such that the two
 * endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
 * with x-axis forms a container, such that the container contains the most water.
 *
 *
 */
public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        if (null == height || height.length < 1) return 0;
        int l = 0, r = height.length - 1;
        int max = 0;
        while (l < r) {
            max = Math.max(max, Math.min(height[l], height[r]) * (r - l + 1));
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max;
    }
}
