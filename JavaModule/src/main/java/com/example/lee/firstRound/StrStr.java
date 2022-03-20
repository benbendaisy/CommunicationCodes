package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 2/26/15.
 *
 * implement strStr().
 *
 * Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 *
 * Update (2014-11-02):
 * The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.
 */
public class StrStr {
    public int strStr(String haystack, String needle) {
        long start = System.currentTimeMillis();
        if (null == haystack || null == needle) {
            return -1;
        } else if (haystack.equals(needle)) {
            return 0;
        }

        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            int j = 0;
            for (; j < needle.length(); j++) {
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    break;
                }
            }
            if (j == needle.length()) {
                long mil = System.currentTimeMillis() - start;
                System.out.println("In m1:" + mil);
                return i;
            }
        }
        return -1;
    }

    public int strStr1(String haystack, String needle) {
        long start = System.currentTimeMillis();
        if (null == haystack || null == needle) {
            return -1;
        } else if (haystack.equals(needle) || needle.length() == 0) {
            return 0;
        }

        int[] next = getNext(needle);

        int j = 0;
        for (int i = 0; i < haystack.length(); i++) {
            while (j > 0 && haystack.charAt(i) != needle.charAt(j)) {
                j = next[j - 1];
            }
            if (haystack.charAt(i) == needle.charAt(j)) {
                j++;
            }
            if (j == needle.length()) {
                long mil = System.currentTimeMillis() - start;
                System.out.println("In m2:" + mil);
                return i - needle.length() + 1;
            }
        }

        return -1;
    }

    public int[] getNext(String pattern) {
        int[] next = new int[pattern.length()];
        int j = 0;
        next[0] = 0;
        for (int i = 1; i < pattern.length(); i++) {
            while (j > 0 && pattern.charAt(j) != pattern.charAt(i)) {
                j = next[j - 1];
            }
            if (pattern.charAt(j) == pattern.charAt(i)) {
                j++;
            }
            next[i] = j;
        }
        return next;
    }

    public static void main(String[] args) {
        StrStr implementstrStr = new StrStr();
        String str = "mississippi";
        String pattern = "issi";
        System.out.println(implementstrStr.strStr(str, pattern));
        System.out.println(implementstrStr.strStr1(str, pattern));
    }
}
