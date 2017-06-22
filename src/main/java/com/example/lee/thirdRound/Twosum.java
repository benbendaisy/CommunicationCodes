package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 6/18/17.
 */
public class Twosum {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        if (nums == null || nums.length == 0) {
            return result;
        }
        Map<Integer, Integer> numsMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (numsMap.containsKey(target - nums[i])) {
                result[0] = numsMap.get(target - nums[i]);
                result[1] = i;
                break;
            } else {
                numsMap.put(nums[i], i);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        Twosum twosum = new Twosum();
        int[] sum = twosum.twoSum(nums, 9);
        System.out.println(sum[0] + ":" + sum[1]);
    }
}
