package com.example.other;

/**
 * Created by benbendaisy on 5/14/15.
 */
public class KMPAlgorithm {
    public int idexOfString(String string, String pattern) {
        if (null == string || null == pattern || string.length() == 0 || pattern.length() == 0) return -1;
        int[] next = getNext(pattern);
        int j = 0;
        for (int i = 0; i < string.length(); i++) {
            while (j > 0 && pattern.charAt(j) != string.charAt(i)) {
                j = next[j - 1];
            }
            if (string.charAt(i) == pattern.charAt(j)) j++;
            if (j == pattern.length()) return i - j + 1;
        }
        return -1;
    }

    private int[] getNext(String pattern) {
        int[] next = new int[pattern.length()];
        int j = 0;
        for (int i = 0; i < pattern.length(); i++) {
            while (j > 0 && pattern.charAt(j) != pattern.charAt(i)) {
                j = next[j - 1];
            }
            if (pattern.charAt(j) == pattern.charAt(i)) j++;
            next[i] = j;
        }
        return next;
    }

    public static void main(String[] args) {
        KMPAlgorithm implementstrStr = new KMPAlgorithm();
        String str = "mississippi";
        String pattern = "ppi";
        //System.out.println(implementstrStr.strStr(str, pattern));
        System.out.println(implementstrStr.idexOfString(str, pattern));
    }
}
