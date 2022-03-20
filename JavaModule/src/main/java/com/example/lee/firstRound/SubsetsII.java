package com.example.lee.firstRound;

import java.util.*;

/**
 * Created by benbendaisy on 1/9/15.
 *
 * Given a collection of integers that might contain duplicates, S, return all possible subsets.
 *
 * Note:
 * Elements in a subset must be in non-descending order.
 * The solution set must not contain duplicate subsets.
 * For example,
 * If S = [1,2,2], a solution is:
 *
 * [
 * [2],
 * [1],
 * [1,2,2],
 * [2,2],
 * [1,2],
 * []
 * ]
 */
public class SubsetsII {
    public List<List<Integer>> subsetsWithDup(int[] num) {
        Set<List<Integer>> sli = new LinkedHashSet<List<Integer>>();
        List<Integer> li = new ArrayList<Integer>();
        sli.add(li);
        if(num == null || num.length == 0){
            return new ArrayList<List<Integer>>();
        }
        Arrays.sort(num);
        for(int i = 0; i < num.length; i++){
            Set<List<Integer>> newLli = new HashSet<List<Integer>>();
            for(List<Integer> list : sli){
                List<Integer> newList = new ArrayList<Integer>(list);
                newList.add(num[i]);
                newLli.add(newList);
            }
            sli.addAll(newLli);
        }
        List<List<Integer>> lli = new ArrayList<List<Integer>>(sli);
        return lli;
    }

    public static void main(String[] args) {
        int[] S = {1, 2, 2};
        SubsetsII subsetsII = new SubsetsII();
        System.out.println(subsetsII.subsetsWithDup(S));
        String s = "";
    }
}
