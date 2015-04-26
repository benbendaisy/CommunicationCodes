package com.example.lee.secondRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 4/23/15.
 */
public class LargestRectangleinHistogram {
    public int largestRectangleArea(int[] height) {
        if (null == height || height.length < 1) return 0;
        int max = 0;
        Stack<Integer> stack = new Stack<Integer>();
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] < height[stack.peek()]) {
                int idx = stack.pop();
                int lMax = (stack.isEmpty() ? i : i - stack.peek() - 1) * height[idx];
                max = Math.max(max, lMax);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            int lMax = (stack.isEmpty() ? height.length : height.length - stack.peek() - 1) * height[idx];
            max = Math.max(max, lMax);
        }
        return max;
    }

    public int largestRectangleAreaI(int[] height) {
        if (null == height || height.length < 1) return 0;
        int max = 0;
        for (int i = 0; i < height.length; i++) {
            int l = i, r = i;
            while (l > 0 && height[l] >= height[i]) {
                l--;
            }
            while (r < height.length && height[r] >= height[i]) {
                r++;
            }
            max = Math.max(max, (r - l) * height[i]);
        }
        return max;
    }
}
