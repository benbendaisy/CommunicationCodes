package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/8/15.
 *
 * Rotate an array of n elements to the right by k steps.
 *
 * For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
 *
 * Note:
 * Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
 *
 * [show hint]
 *
 * Hint:
 * Could you do it in-place with O(1) extra space?
 *
 */
public class RotateArray {

    //o(n^2)
    public void rotate(int[] nums, int k) {
        if (null == nums || k < 1) {
            return;
        }
        k = k % nums.length;
        for (int i = 0; i < k; i++) {
            int idx = 0;
            int t = nums[0];
            while (idx < nums.length - 1) {
                nums[idx] = nums[idx + 1];
                idx++;
            }
            nums[idx] = t;
        }
    }

    //ab cde fgh -> ab fgh cde->fgh ab cde o(n) solution
    //swap k characters until less than k characters left, then rotate
    public void rotateI(int[] nums, int k) {
        if (null == nums || nums.length < 2 || k < 1 || nums.length == k) {
            return;
        }

        if (null == nums || k < 1) {
            return;
        }
        k = k % nums.length;

        int idx = nums.length - 1;
        while (idx - 2 * k >= 0) {
            for (int i = idx; i > idx - k; i--) {
                swap(nums, i, i - k);
            }
            idx -= k;
        }

        int left = idx - k + 1;
        for (int i = 0; i < left; i++) {
            int idy = idx - k;
            while (idy < idx) {
                swap(nums, idy, idy + 1);
                idy++;
            }
            idx--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        RotateArray rotateArray = new RotateArray();
        int[] nums = {1, 2, 3};
        rotateArray.rotateI(nums, 2);
        System.out.println(nums);
    }
}
