package com.example.lee.thirdRound;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by benbendaisy on 7/8/17.
 */
public class PermutationsII {
    public List<List<Integer>> permuteUnique(int[] nums) {
        if (nums == null || nums.length == 0) {
            return Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        for (int i = 0; i < nums.length; i++) {
            Set<List<Integer>> resSet = new HashSet<>();
            for (List list : res) {
                for (int j = 0; j < list.size() + 1; j++) {
                    list.add(j, nums[i]);
                    resSet.add(new ArrayList<>(list));
                    list.remove(j);
                }
            }
            res = new ArrayList<>(resSet);
        }
        return res;
    }
    /**
     * did not pass leet code because of 'Time Limit'
     * @param nums
     * @return
     */
    public List<List<Integer>> permuteUniqueI(int[] nums) {
        if (nums == null || nums.length == 0) {
            return Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        permuteHelper(nums, 0, res);
        return res.stream().distinct().collect(Collectors.toList());
    }

    private void permuteHelper(int[] nums, int idx, List<List<Integer>> res) {
        if (idx == nums.length) {
            List<Integer> list = IntStream.of(nums).boxed().collect(Collectors.toList());
            res.add(list);
            return;
        }
        for (int i = idx; i < nums.length; i++) {
            swap(nums, i, idx);
            permuteHelper(nums, idx + 1, res);
            swap(nums, i, idx);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        int[] nums = {-1,2,0,-1,1,0,1};
        PermutationsII permutationsII = new PermutationsII();
        permutationsII.permuteUnique(nums).stream().forEach(System.out::println);
    }
}
