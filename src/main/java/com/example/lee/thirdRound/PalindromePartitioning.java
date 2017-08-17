package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PalindromePartitioning {
    public List<List<String>> partition(String s) {
        if (s == null || s.length() == 0) {
            return Collections.emptyList();
        }
        List<List<String>> lists = new ArrayList<>();
        partition(s, 0, new ArrayList<>(), lists);
        return lists;
    }

    private void partition(String str, int idx, List<String> list, List<List<String>> lists) {
        if (idx == str.length()) {
            lists.add(list);
            return;
        }
        for (int i = idx; i <= str.length(); i++) {
            String temp = str.substring(idx, i);
            if (isValidPalindrome(temp)) {
                List<String> newList = new ArrayList<>(list);
                newList.add(temp);
                partition(str, i, newList, lists);
            }
        }
    }

    private boolean isValidPalindrome(String str) {
        if (str.isEmpty()) {
            return false;
        }
        int l = 0, r = str.length() - 1;
        while (l < r) {
            if (str.charAt(l) != str.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    public static void main(String[] args) {
        PalindromePartitioning palindromePartitioning = new PalindromePartitioning();
        palindromePartitioning.partition("aab").stream().forEach(System.out::println);
    }

}
