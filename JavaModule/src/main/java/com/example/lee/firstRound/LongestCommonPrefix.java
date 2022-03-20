package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/3/15.
 */
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if (null == strs || strs.length == 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }

        String str = strs[0];
        int idxMax = str.length();
        for (int i = 1; i < strs.length; i++) {
            int lIdx = findLongestCommonPrefix(strs[i], str);
            if (idxMax > lIdx) {
                idxMax = lIdx;
            }
        }
        return str.substring(0, idxMax);
    }

    private int findLongestCommonPrefix(String str1, String str2) {
        if (null == str1 || null == str2 || str1.length() == 0 || str2.length() == 0) {
            return 0;
        }
        int idx = 0;
        int minL = Math.min(str1.length(), str2.length());
        while (idx < minL && str1.charAt(idx) == str2.charAt(idx)) {
            idx++;
        }
        return idx;
    }

    public static void main(String[] args) {
        String[] strs = {"a", "b", "a"};
        LongestCommonPrefix longestCommonPrefix = new LongestCommonPrefix();
        System.out.println(longestCommonPrefix.findLongestCommonPrefix("a","b"));
        System.out.println(longestCommonPrefix.longestCommonPrefix(strs));
        System.out.println("a".substring(0, 0));
    }
}
