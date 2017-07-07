package com.example.lee.thirdRound;

import java.util.Optional;
import java.util.stream.IntStream;

/**
 * Created by benbendaisy on 7/6/17.
 */
public class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        if (nums == null || nums.length < 1) {
            return 1;
        } else if (nums.length == 1) {
            return nums[0] == 1 ? 2 : 1;
        }
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i && nums[i] < nums.length && nums[i] > 0 && nums[nums[i]] != nums[i]) {
                swap(nums, i, nums[i]);
            }
        }
        Optional<Integer> missingIntegerOpt = IntStream.range(1, nums.length)
                .boxed()
                .filter(i -> nums[i] != i)
                .findAny();
        return missingIntegerOpt.isPresent() ?
                missingIntegerOpt.get() : (nums[0] == nums.length ? nums.length + 1 : nums.length);
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        FirstMissingPositive firstMissingPositive = new FirstMissingPositive();
        int[] nums = {1, 0};
        System.out.println(firstMissingPositive.firstMissingPositive(nums));
    }
}
