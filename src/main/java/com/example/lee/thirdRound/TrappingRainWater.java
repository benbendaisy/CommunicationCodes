package com.example.lee.thirdRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 7/7/17.
 */
public class TrappingRainWater {
    /**
     * O(n^2) solution, brute force and passed leet code
     * @param height
     * @return
     */
    public int trap(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        int ans = 0;
        for (int i = 0; i < height.length; i++) {
            //left max
            int leftMax = 0;
            for (int j = 0; j <= i; j++) {
                leftMax = Math.max(leftMax, height[j]);
            }
            // right max
            int rightMax = 0;
            for (int j = height.length - 1; j >= i; j--) {
                rightMax = Math.max(rightMax, height[j]);
            }
            ans += Math.min(leftMax, rightMax) - height[i];
        }
        return ans;
    }

    /**
     * O(n) solution passed leet code
     * @param height
     * @return
     */
    public int trapI(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        int[] leftMax = new int[height.length];
        int[] rightMax = new int[height.length];

        // find left maxes
        leftMax[0] = height[0];
        for (int i = 1; i < height.length; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i]);
        }

        // find right maxes
        rightMax[height.length - 1] = height[height.length - 1];
        for (int i = height.length - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i]);
        }

        int res = 0;
        for (int i = 0; i < height.length; i++) {
            res += Math.min(leftMax[i], rightMax[i]) - height[i];
        }
        return res;
    }

    /**
     * O(n) solution with stack to save index of height
     * refer to: https://leetcode.com/articles/trapping-rain-water/
     * @param height
     * @return
     */
    public int trapII(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[stack.peek()] < height[i]) {
                int top = stack.peek();
                stack.pop();
                if (stack.isEmpty()) {
                    continue;
                }
                int dist = i - stack.peek() - 1;
                int h = Math.min(height[stack.peek()], height[i]) - height[top];
                res += dist * h;
            }
            stack.push(i);
        }
        return res;
    }

    public int trapIII(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        int leftMax = 0, rightMax = 0;
        int l = 0, r = height.length - 1;
        int res = 0;
        while (l < r) {
            if (height[l] < height[r]) {
                if (leftMax > height[l]) {
                    res += leftMax - height[l];
                } else {
                    leftMax = height[l];
                }
                l++;
            } else {
                if (rightMax > height[r]) {
                    res += rightMax - height[r];
                } else {
                    rightMax = height[r];
                }
                r--;
            }
        }
        return res;
    }

}
