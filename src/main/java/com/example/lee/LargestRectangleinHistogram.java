package com.example.lee;

import java.util.Stack;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
 *
 * Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
 *
 * The largest rectangle is shown in the shaded area, which has area = 10 unit.
 *
 * For example,
 * Given height = [2,1,5,6,2,3],
 * return 10.
 *
 */
public class LargestRectangleinHistogram {

    //o(n) stack is used to store index that is less than current height
    public int largestRectangleArea(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }

        Stack<Integer> stack = new Stack<Integer>();
        int max = 0;
        for(int i = 0; i < height.length; i++){
            int localArea = 0;
            while(!stack.isEmpty() && height[stack.peek()] > height[i]){
                int localIndex = stack.pop();
                localArea = stack.isEmpty() ? i * height[localIndex] : (i - stack.peek() - 1) * height[localIndex];
                max = Math.max(max, localArea);
            }
            stack.push(i);
        }

        while(!stack.isEmpty()){
            int localIndex = stack.pop();
            int localArea = stack.isEmpty() ? height.length * height[localIndex] : (height.length - stack.peek() - 1) * height[localIndex];
            max = Math.max(max, localArea);
        }
        return max;
    }

    //O(n^2) starting from current and extend it to left and right to find most rectangle
    //that current height can have
    public int largestRectangleAreaI(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }

        Stack<Integer> stack = new Stack<Integer>();
        int max = 0;
        for(int i = 0; i < height.length; i++){
            int left = i, right = i;
            while(left > 0 && right < height.length){
                int hasMore = 0;
                if(height[left] >= height[i]){
                    left--;
                    hasMore++;
                }
                if(height[right] >= height[i]){
                    right++;
                    hasMore++;
                }
                if(hasMore == 0){
                    break;
                }
            }
            int localArea = (right - left) * height[i];
            max = Math.max(max, localArea);
        }
        return max;
    }
}
