package com.example.lee;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 2/5/15.
 *
 * Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
 *
 * Each number in C may only be used once in the combination.
 *
 * Note:
 * All numbers (including target) will be positive integers.
 * Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
 * The solution set must not contain duplicate combinations.
 * For example, given candidate set 10,1,2,7,6,1,5 and target 8,
 * A solution set is:
 * [1, 7]
 * [1, 2, 5]
 * [2, 6]
 * [1, 1, 6]
 */
public class CombinationSumII {
    public List<List<Integer>> combinationSum2(int[] num, int target) {
        List<List<Integer>> lists = new ArrayList<List<Integer>>();
        if(null == num || num.length == 0 || target < 0){
            return lists;
        }
        List<Integer> list = new ArrayList<Integer>();
        Arrays.sort(num);
        combinationSum(num, target, 0, list, lists);
        return lists;
    }

    public void combinationSum(int[] num, int target, int idx, List<Integer> list, List<List<Integer>> lists) {
        if(target == 0){
            if(!containsList(list, lists)){
                lists.add(list);
            }
        } else if(target < 0 || idx >= num.length){
            return;
        }

        for(int i = idx; i < num.length; i++){
            List<Integer> newList = new ArrayList<>(list);
            newList.add(num[i]);
            combinationSum(num, target - num[i], i + 1, newList, lists);
        }
    }

    private boolean containsList(List<Integer> list, List<List<Integer>> lists){
        for(List<Integer> li : lists){
            if(list.size() == li.size()){
                int i = 0;
                for(; i < list.size(); i++){
                    if(li.get(i) != list.get(i)){
                        break;
                    }
                }
                if(i == list.size()){
                    return true;
                }
            }
        }
        return false;
    }
}
