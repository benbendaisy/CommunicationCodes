package com.example.lee.thirdRound;

import java.util.Map;
import java.util.Stack;

/**
 * Created by benbendaisy on 7/16/17.
 */
public class LargestRectangleInHistogram {
    public int largestRectangleArea(int[] heights) {
        if (heights == null || heights.length < 1) {
            return 0;
        }
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        for (int i = 0; i < heights.length; i++) {
            while (!stack.isEmpty() && heights[stack.peek()] > heights[i]) {
                int idx = stack.pop();
                int localMax = stack.isEmpty() ? i * heights[idx] : (i - stack.peek() - 1) * heights[idx];
                maxArea = Math.max(maxArea, localMax);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            int localMax = stack.isEmpty() ? heights.length * heights[idx] : (heights.length - stack.peek() - 1) * heights[idx];
            maxArea = Math.max(localMax, maxArea);
        }
        return maxArea;
    }

    public static void main(String[] args) {
        LargestRectangleInHistogram largestRectangleInHistogram = new LargestRectangleInHistogram();
        int[] heights = {9, 0};
        System.out.println(largestRectangleInHistogram.largestRectangleArea(heights));
    }
}
