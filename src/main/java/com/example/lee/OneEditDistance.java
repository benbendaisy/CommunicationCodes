package com.example.lee;

/**
 * Created by benbendaisy on 3/7/15.
 *
 * Given two strings S and T, determine if they are both one edit distance apart.
 *
 * refer to http://www.danielbit.com/blog/puzzle/leetcode/leetcode-one-edit-distance
 */
public class OneEditDistance {
    public boolean isOneEditDistance(String s, String t) {
        if (null == s || null == t || Math.abs(s.length() - t.length()) > 1) {
            return false;
        }

        int m = s.length();
        int n = t.length();

        int idxs = 0;
        int idxt = 0;
        while (idxs < m && idxt < n && s.charAt(idxs) == t.charAt(idxt)) {
            idxs++;
            idxt++;
        }
        if (m == idxs && n == idxt) {
            return true;
        } else if (m == n) {
            idxs++;
            idxt++;
        } else {
            if (m > n) {
                idxs++;
            } else {
                idxt++;
            }
        }

        while (idxs < m && idxt < n && s.charAt(idxs) == t.charAt(idxt)) {
            idxs++;
            idxt++;
        }

        return idxs == m && idxt == n;
    }
}
