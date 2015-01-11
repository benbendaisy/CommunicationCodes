package com.example.lee;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

/**
 * Created by benbendaisy on 1/9/15.
 *
 * Given a set of distinct integers, S, return all possible subsets.
 *
 * Note:
 * Elements in a subset must be in non-descending order.
 * The solution set must not contain duplicate subsets.
 * For example,
 * If S = [1,2,3], a solution is:
 *
 * [
 * [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 */
public class Subsets {

    //iterative solution
    public List<List<Integer>> subsets(int[] S) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        List<Integer> li = new ArrayList<Integer>();
        lli.add(li);
        if(S == null || S.length == 0){
            return lli;
        }
        Arrays.sort(S);
        for(int i = 0; i < S.length; i++){
            List<List<Integer>> newLli = new ArrayList<List<Integer>>();
            for(List<Integer> list : lli){
                List<Integer> newList = new ArrayList<Integer>(list);
                newList.add(S[i]);
                newLli.add(newList);
            }
            lli.addAll(newLli);
        }
        return lli;
    }


    //recursive solution
    public List<List<Integer>> subsetsI(int[] S) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        List<Integer> li = new ArrayList<Integer>();
        lli.add(li);
        if(S == null || S.length == 0){
            return lli;
        }
        Arrays.sort(S);
        subsetsHelper(S, 0, lli);
        return lli;
    }
    private void subsetsHelper(int[] S, int index, List<List<Integer>> lli){
        if(index == S.length){
            return;
        }
        List<List<Integer>> newLli = new ArrayList<List<Integer>>();
        for(List<Integer> list : lli){
            List<Integer> newList = new ArrayList<Integer>(list);
            newList.add(S[index]);
            newLli.add(newList);
        }
        lli.addAll(newLli);

        subsetsHelper(S, ++index, lli);
    }

    public static void main(String[] args) {
        int[] S = {1, 2, 3};
        Subsets subsets = new Subsets();
        System.out.println(subsets.subsetsI(S));
    }
}
