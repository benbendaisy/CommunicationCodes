package com.example.lee.thirdRound;

import java.util.stream.IntStream;

/**
 * Created by benbendaisy on 7/2/17.
 */
public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            while (r > l && nums[r] == val) {
                r--;
            }
            if (l == r) {
                break;
            }
            if (nums[l] == val) {
                nums[l] = nums[r];
                nums[r] = val;
                r--;
            }
            l++;

        }
        return nums[l] == val ? l : l + 1;
    }

    public static void main(String[] args) {
        RemoveElement removeElement = new RemoveElement();
        int[] nums = {3, 2, 2, 3};
        int l = removeElement.removeElement(nums, 3);
        IntStream.range(0, l).forEach(i -> System.out.println(nums[i]));
    }
}
