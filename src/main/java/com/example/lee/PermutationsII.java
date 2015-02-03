package com.example.lee;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 2/1/15.
 *
 * given a collection of numbers that might contain duplicates, return all possible unique permutations.
 *
 * For example,
 * [1,1,2] have the following unique permutations:
 * [1,1,2], [1,2,1], and [2,1,1]
 */
public class PermutationsII {
    public List<List<Integer>> permuteUnique(int[] num) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if(null == num){
            return lli;
        }
        permuteUnique(num, lli, 0);
        return lli;
    }

    private void permuteUnique(int[] num, List<List<Integer>> lli, int idx){
        if(idx == num.length){
            if(!containsSame(num, lli)){
                List<Integer> li = new ArrayList<Integer>();
                for(int i : num){
                    li.add(i);
                }
                lli.add(li);
            }
            return;
        }

        for(int i = idx; i < num.length; i++){
            swap(num, i, idx);
            permuteUnique(num, lli, idx + 1);
            swap(num, i, idx);
        }
    }

    private void swap(int[] num, int i, int j){
        int temp = num[i];
        num[i] = num[j];
        num[j] = temp;
    }

    private boolean containsSame(int[] num, List<List<Integer>> lli){
        if(lli.size() == 0){
            return false;
        }
        for(List<Integer> li : lli){
            if(num.length != li.size()){
                continue;
            }

            int idx = 0;
            while(idx < num.length){
                if(num[idx] != li.get(idx)){
                    break;
                }
                idx++;
            }
            if(idx == num.length){
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        PermutationsII permutationsII = new PermutationsII();
        int[] num = {3,3,0,0,2,3,2};
        List<List<Integer>> lli = permutationsII.permuteUnique(num);

        for(List<Integer> li : lli){
            System.out.println(li);
        }
    }
}
