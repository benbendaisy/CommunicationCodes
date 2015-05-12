package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/11/15.
 */
public class SortColors {
    public void sortColors(int[] nums) {
        if (null == nums || nums.length < 2) return;
        int p0 = 0;
        int len = nums.length;
        while (p0 < len && nums[p0] == 0) p0++;
        int p1 = p0, p2 = len - 1;
        while (p1 <= p2) {
            while (p1 <= p2 && nums[p1] == 1) p1++;
            while (p1 <= p2 && nums[p2] == 2) p2--;
            if (p1 <= p2) {
                if (nums[p1] == 2) {
                    swap(nums, p1, p2);
                } else {
                    swap(nums, p0, p1);
                    p0++;
                    p1++;
                }
            }
        }
    }

    private void swap(int[] nums, int l, int r) {
        int t = nums[l];
        nums[l] = nums[r];
        nums[r] = t;
    }

    public static void main(String[] args) {
        SortColors sortColors = new SortColors();
        int[] nums = {2, 2};
        sortColors.sortColors(nums);
        System.out.println(nums);
    }
}
