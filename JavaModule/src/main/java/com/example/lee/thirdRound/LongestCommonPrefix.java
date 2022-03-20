package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null) {
            return null;
        } else if (strs.length == 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }
        int l = 0;
        while (true) {
            if (strs[0].length() <= l) {
                break;
            }
            char ch = strs[0].charAt(l);
            boolean isSame = true;
            for (int i = 1; i < strs.length; i++) {
                if (strs[i].length() <= l || strs[i].charAt(l) != ch) {
                    isSame = false;
                    break;
                }
            }
            if (!isSame) {
                break;
            }
            l++;
        }
        return strs[0].substring(0, l);
    }
}
