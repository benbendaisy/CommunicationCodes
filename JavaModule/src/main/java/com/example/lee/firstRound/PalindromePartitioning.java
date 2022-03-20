package com.example.lee.firstRound;

import java.util.*;

/**
 * Created by benbendaisy on 12/23/14.
 * Given a string s, partition s such that every substring of the partition is a palindrome.
 * Return all possible palindrome partitioning of s.
 * For example, given s = "aab",
 * Return
 * [
 * ["aa","b"],
 * ["a","a","b"]
 * ]
 */
public class PalindromePartitioning {
    public List<List<String>> partition(String s) {
        List<List<String>> lls = new ArrayList<List<String>>();
        if(s == null || s.isEmpty()){
            return lls;
        } else if(s.length() == 1){
            List<String> ls = new ArrayList<String>();
            ls.add(s);
            lls.add(ls);
            return lls;
        }

        int len = s.length();
        boolean[] wb = new boolean[len + 1];
        Map<Integer, Set<Integer>> map = new HashMap<Integer, Set<Integer>>();
        for(int i = 1; i <= len; i++){
            if(isPalindrome(s.substring(0, i))){
                wb[i] = true;
                Set<Integer> li;
                if(map.containsKey(i)){
                    li = map.get(i);
                } else {
                    li = new LinkedHashSet<Integer>();
                    map.put(i, li);
                }
                li.add(0);
            }

            if(wb[i]){
                for(int j = i + 1; j <= len; j++){
                    String subStr = s.substring(i, j);
                    if(isPalindrome(subStr)){
                        wb[j] = true;
                        Set<Integer> li;
                        if(map.containsKey(j)){
                            li = map.get(j);
                        } else {
                            li = new LinkedHashSet<Integer>();
                            map.put(j, li);
                        }
                        li.add(i);
                    }
                }
            }
        }
        List<String> ls = new ArrayList<String>();
        getAllPartitions(s, map, len, ls, lls);
        return lls;
    }

    private boolean isPalindrome(String s){
        if(s == null || s.isEmpty() || s.length() == 1){
            return true;
        }
        int len = s.length();
        int left, right;
        left = len / 2 - 1;
        if(len % 2 == 0){
            right = left + 1;
        } else {
            right = left + 2;
        }
        while(left >= 0 && right < len){
            if(s.charAt(left) != s.charAt(right)){
                return false;
            }
            left--;
            right++;
        }
        return true;
    }

    private boolean isPalindromeI(String s){
        if(s == null || s.isEmpty() || s.length() == 1){
            return true;
        }
        int len = s.length();
        int left = 0, right = len - 1;

        while(left < right){
            if(s.charAt(left) != s.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private void getAllPartitions(String s, Map<Integer, Set<Integer>> map, int index, List<String> candidates, List<List<String>> lls){
        if(!map.containsKey(index)){
            candidates.add(0, s.substring(0, index));
            lls.add(candidates);
        } else {
            Set<Integer> prevs = map.get(index);
            for(int prev : prevs){
                List<String> ls = new ArrayList<String>();
                ls.addAll(candidates);
                ls.add(0, s.substring(prev, index));
                if(prev > 0){
                    getAllPartitions(s, map, prev, ls, lls);
                } else {
                    lls.add(ls);
                }
            }
        }
    }

    public static void main(String[] args) {
        PalindromePartitioning palindromePartitioning = new PalindromePartitioning();
        System.out.println(palindromePartitioning.partition("dde"));
    }
}
