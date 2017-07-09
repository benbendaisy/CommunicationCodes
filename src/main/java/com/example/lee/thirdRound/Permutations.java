package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Created by benbendaisy on 7/8/17.
 */
public class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        if (nums == null || nums.length < 1) {
            return Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();
        permuteHelper(nums, 0, res);
        return res;
    }

    /**
     * I use stream to create list but it seems very slow when it runs on leetcode.
     * Want to know why?
     * @param nums
     * @param idx
     * @param res
     */
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

    /**
     * both passed leet code. However, it seems permuteI is faster although its time complexity is higher.
     * I am guessing that the issue is that 'IntStream.of' is slow.
     * Then, guessing all streaming is slower in Java8 than for loop.
     * @param nums
     * @return
     */
    public List<List<Integer>> permuteI(int[] nums) {
        if (nums == null || nums.length == 0) {
            Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        for (int i = 0; i < nums.length; i++) {
            List<List<Integer>> newRes = new ArrayList<>();
            for (List<Integer> list : res) {
                for (int j = 0; j < list.size() + 1; j++) {
                    list.add(j, nums[i]);
                    newRes.add(new ArrayList<>(list));
                    list.remove(j);
                }
            }
            res = newRes;
        }
        return res;
    }

    public static void main(String[] args) {
        Permutations permutations = new Permutations();
        int[] nums = {1, 2, 3};
        permutations.permute(nums).stream().forEach(System.out::println);
    }
}
