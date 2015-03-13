package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/14/15.
 * Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
 *
 * For example,
 * If n = 4 and k = 2, a solution is:
 *
 * [
 * [2,4],
 * [3,4],
 * [2,3],
 * [1,2],
 * [1,3],
 * [1,4],
 * ]
 */
public class Combinations {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if(n == 0 || n < k || k == 0){
            return lli;
        }
        List<Integer> li = new ArrayList<Integer>();
        combine(n, k, 1, lli, li);
        return lli;
    }

    private void combine(int n, int k, int index, List<List<Integer>> lli, List<Integer> li){
        if(k == li.size()){
            lli.add(li);
            return;
        } else if(index > n){
            return;
        }

        for(int i = index; i <= n; i++){
            List<Integer> newLi = new ArrayList<Integer>(li);
            newLi.add(i);
            combine(n, k, i + 1, lli, newLi);
        }
    }

    public static void main(String[] args) {
        Combinations combinations = new Combinations();
        System.out.println(combinations.combine(1, 1));
    }
}
