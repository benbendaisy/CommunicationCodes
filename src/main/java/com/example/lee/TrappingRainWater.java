package com.example.lee;

/**
 * Created by benbendaisy on 2/3/15.
 * Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
 *
 * For example,
 * Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
 *
 *
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
 */
public class TrappingRainWater {
    public int trap(int[] A) {
        if(null == A || A.length < 2){
            return 0;
        }

        //int left = 0, right = A.length - 1;
        int leftMax = 0;
        int[] left = new int[A.length];
        for(int i = 0; i < A.length; i++){
            leftMax = Math.max(leftMax, A[i]);
            left[i] = leftMax;
        }
        int rightMax = 0, maxArea = 0;
        for(int i = A.length - 1; i >= 0; i--){
            rightMax = Math.max(A[i], rightMax);
            int min = Math.min(left[i], rightMax);
            if(min > A[i]){
                maxArea += min - A[i];
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        TrappingRainWater trappingRainWater = new TrappingRainWater();
        int[] A = {4,2,0,3,2,4,3,4};
        System.out.println(trappingRainWater.trap(A));
    }
}
