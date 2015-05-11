package com.example.lee.secondRound;

import com.example.lee.model.Interval;

import java.util.*;

/**
 * Created by benbendaisy on 4/19/15.
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
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == num || num.length == 0) return lli;
        Arrays.sort(num);
        Set<List<Integer>> sli = new HashSet<List<Integer>>();
        sli.add(new ArrayList<Integer>());
        for (int i = 0; i < num.length; i++) {
            Set<List<Integer>> newSli = new HashSet<List<Integer>>();
            for (List<Integer> list : sli) {
                List<Integer> newList = new ArrayList<Integer>(list);
                newList.add(num[i]);
                newSli.add(newList);
            }
            sli.addAll(newSli);
        }
        lli.addAll(sli);
        return lli;
    }

    //the order is not right
    public List<List<Integer>> subsetsWithDupI(int[] num) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == num || num.length == 0) return lli;
        Set<List<Integer>> sli = new HashSet<List<Integer>>();
        Arrays.sort(num);
        subsetsWithDup(num, 0, sli);
        lli.addAll(sli);
        return lli;
    }

    private void subsetsWithDup(int[] num, int idx, Set<List<Integer>> sli) {
        if (idx == num.length) {
            List<Integer> li = new ArrayList<Integer>();
            sli.add(li);
        }
        subsetsWithDup(num, idx + 1, sli);
        Set<List<Integer>> newSli = new HashSet<List<Integer>>();
        for (List<Integer> list : sli) {
            List<Integer> li = new ArrayList<Integer>(list);
            li.add(0, num[idx]);
            newSli.add(li);
        }
        sli.addAll(newSli);
    }
}
