package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/5/15.
 */
public class PalindromePartitioning {
    public List<List<String>> partition(String s) {
        List<List<String>> lls = new ArrayList<List<String>>();
        if (null == s) return lls;
        List<String> ls = new ArrayList<String>();
        partitionHelp(s, lls, ls);
        return lls;
    }

    private void partitionHelp(String s, List<List<String>> lls, List<String> ls) {
        if ("".equals(s)) {
            lls.add(ls);
            return;
        } else if (s.length() == 1) {
            ls.add(s);
            lls.add(ls);
            return;
        }
        for (int i = 1; i <= s.length(); i++) {
            String str = s.substring(0, i);
            if (isPalindrome(str)) {
                List<String> newLs = new ArrayList<String>();
                newLs.addAll(ls);
                newLs.add(str);
                partitionHelp(s.substring(i), lls, newLs);
            }
        }
    }

    private boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
