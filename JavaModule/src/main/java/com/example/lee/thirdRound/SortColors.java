package com.example.lee.thirdRound;

import java.util.stream.Stream;

/**
 * Created by benbendaisy on 7/15/17.
 */
public class SortColors {
    public void sortColors(int[] nums) {
        if (nums == null || nums.length < 2) {
            return;
        }
        int idx1 = 0, idx2 = 0, idx3 = nums.length - 1;
        while (idx1 < nums.length && nums[idx1] == 0) {
            idx1++;
        }
        idx2 = idx1;
        while (idx1 <= idx2 && idx2 <= idx3) {
            while (idx2 <= idx3 && nums[idx2] == 1) {
                idx2++;
            }
            while (idx3 >= idx2 && nums[idx3] == 2) {
                idx3--;
            }

            if (idx2 <= idx3 && idx1 <= idx2) {
                swap(nums, idx2, idx3);
                if (nums[idx2] == 1) {
                    idx2++;
                } else if (nums[idx2] == 2) {
                    swap(nums, idx2, idx3);
                    idx3--;
                } else if (nums[idx2] == 0) {
                    swap(nums, idx2, idx1);
                    idx1++;
                    idx2++;
                }
            }
        }
    }

    public void sortColorsI(int[] nums) {
        if (nums == null || nums.length < 2) {
            return;
        }

        int[] idxs = new int[3];
        for (int num : nums) {
            idxs[num]++;
        }
        int i = 0;
        setColors(nums, 0, idxs[0] - 1, 0);
        setColors(nums, idxs[0], idxs[0] + idxs[1] - 1, 1);
        setColors(nums, idxs[0] + idxs[1], nums.length - 1, 2);
    }

    private void setColors(int[] nums, int idx1, int idx2, int num) {
        for (int i = idx1; i < nums.length; i++) {
            nums[i] = num;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        SortColors sortColors = new SortColors();
        int[] nums = {2,2,0,0,2,0,2,1,0};
        sortColors.sortColors(nums);
        for (int i : nums) {
            System.out.print(i + ", ");
        }
//        Stream.of(nums).forEach(i -> System.out.print(i.toString() + ", "));
    }
}
