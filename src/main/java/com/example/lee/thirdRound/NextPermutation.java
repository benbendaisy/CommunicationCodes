package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/4/17.
 */
public class NextPermutation {
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return;
        }
        int idx = nums.length - 1;
        while (idx > 0 && nums[idx] <= nums[idx - 1]) {
            idx--;
        }
        // it's already the smallest that just need to swap the last two digits
        if (idx == nums.length - 1) {
            swap(nums, idx, idx - 1);
            return;
        }

        // find the inflection point(拐点) like 1 < 3 > 2
        if (idx > 0 && nums[idx - 1] < nums[idx]) {
            // find the number that is just greater than the num of idx - 1
            // and swap them
            int k = nums.length - 1;
            while (k >= idx && nums[k] <= nums[idx - 1]) {
                k--;
            }
            swap(nums, k, idx - 1);
        }
        int l = idx, r = nums.length - 1;
        while (l < r) {
            swap(nums, l, r);
            l++;
            r--;
        }
    }
    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        NextPermutation nextPermutation = new NextPermutation();
        int[] nums = {4,2,0,2,3,2,0};
        nextPermutation.nextPermutation(nums);
    }
}
