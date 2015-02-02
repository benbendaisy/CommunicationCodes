package com.example.lee;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/23/15.
 *
 * The set [1,2,3,…,n] contains a total of n! unique permutations.
 *
 * By listing and labeling all of the permutations in order,
 * We get the following sequence (ie, for n = 3):
 *
 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 * Given n and k, return the kth permutation sequence.
 *
 * Note: Given n will be between 1 and 9 inclusive.
 */
public class PermutationSequence {
    public String getPermutation(int n, int k) {
        if(n < 0 || k < 0 || n > 9){
            return "";
        }

        char[] ch = new char[n];
        for(int i = 1; i <= n; i++){
            ch[i - 1] = (char) (i + '0');
        }

        List<String> list = new ArrayList<String>();
        getPermutation(ch, 0, list);
        if(list.size() > k){
            return list.get(k);
        }
        return "";
    }

    private void getPermutation(char[] ch, int index,  List<String> list){
        if(index >= ch.length){
            list.add(new String(ch));
            System.out.println(ch);
        }
        for(int i = index; i < ch.length; i++){
            swap(ch, index, i);
            getPermutation(ch, index + 1, list);
            swap(ch, index, i);
        }
    }

    private void swap(char[] ch, int i, int j){
        char c = ch[i];
        ch[i] = ch[j];
        ch[j] = c;
    }

    public static void main(String[] args) {
        PermutationSequence permutationSequence = new PermutationSequence();
        System.out.println(permutationSequence.getPermutation(9, 9));
    }
}
