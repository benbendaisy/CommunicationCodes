package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        int l = 0;
        int r = height.length - 1;
        int maxArea = 0;
        while (l < r) {
            int localArea = Math.min(height[l], height[r]) * (r - l);
            maxArea = Math.max(maxArea, localArea);
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
}
