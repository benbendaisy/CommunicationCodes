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
        int len = height.length;
        for (int i = 0; i < len; i++) {
            while (!stack.isEmpty() && height[stack.peek()] > height[i]) {
                int idx = stack.pop();
                max = Math.max(max, (stack.isEmpty() ? i : i - stack.peek() - 1) * height[idx]);
            }
            stack.push(i);
        }

        while (!stack.isEmpty()) {
            int idx = stack.pop();
            max = Math.max(max, (stack.isEmpty() ? len : len - stack.peek() - 1) * height[idx]);
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
