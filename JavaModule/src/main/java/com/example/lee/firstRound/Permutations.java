package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Created by benbendaisy on 2/1/15.
 *
 * Given a collection of numbers, return all possible permutations.
 *
 * For example,
 * [1,2,3] have the following permutations:
 * [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
 */
public class Permutations {
    public List<List<Integer>> permute(int[] num) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if(num == null || num.length == 0){
            return lli;
        }

        permute(num, lli, 0);
        return lli;
    }

    private void permute(int[] num, List<List<Integer>> lli, int index){
        if(index == num.length){
            List<Integer> li = new ArrayList<Integer>();
            for(int i : num){
                li.add(i);
            }
            lli.add(li);
            return;
        }
        for(int i = index; i < num.length; i++){
            swap(num, i, index);
            permute(num, lli, index + 1);
            swap(num, i, index);
        }
    }

    private void swap(int[] num, int i, int j){
        int t = num[i];
        num[i] = num[j];
        num[j] = t;
    }
}
