package com.example.lee.firstRound;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 3/8/15.
 *
 * Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
 *
 * Below is one possible representation of s1 = "great":
 *
 *  great
 *  /    \
 * gr    eat
 * / \    /  \
 * g   r  e   at
 * / \
 * a   t
 * To scramble the string, we may choose any non-leaf node and swap its two children.
 *
 * For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
 *
 * rgeat
 * /    \
 * rg    eat
 * / \    /  \
 * r   g  e   at
 * / \
 * a   t
 * We say that "rgeat" is a scrambled string of "great".
 *
 * Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
 *
 * rgtae
 * /    \
 * rg    tae
 * / \    /  \
 * r   g  ta  e
 * / \
 * t   a
 * We say that "rgtae" is a scrambled string of "great".
 *
 * Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
 */
public class ScrambleString {
    public boolean isScramble(String s1, String s2) {
        if (null == s1 && null == s2) {
            return true;
        } else if (null == s1 || null == s2 || s1.length() != s2.length()) {
            return false;
        } else if (s1.equals(s2)) {
            return true;
        }
        int L = s1.length();

        if (!isStringsEqual(s1, s2)) {
            return false;
        }

        for (int i = 1; i < L; i++) {
            String s11 = s1.substring(0, i);
            String s12 = s1.substring(i);
            String s21 = s2.substring(0, i);
            String s22 = s2.substring(i);
            if (isScramble(s11, s21) && isScramble(s12, s22)) {
                return true;
            }

            s21 = s2.substring(L - i);
            s22 = s2.substring(0, L - i);
            if (isScramble(s11, s21) && isScramble(s12, s22)) {
                return true;
            }

        }
        return false;
    }

    //o(n)
    private boolean isStringsEqual(String str1, String str2) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < str1.length(); i++) {
            if (map.containsKey(str1.charAt(i))) {
                map.put(str1.charAt(i), map.get(str1.charAt(i)) + 1);
            } else {
                map.put(str1.charAt(i), 1);
            }
        }

        for (int i = 0; i < str2.length(); i++) {
            if (!map.containsKey(str2.charAt(i)) || map.get(str2.charAt(i)) < 1) {
                return false;
            } else {
                map.put(str2.charAt(i), map.get(str2.charAt(i)) - 1);
            }
        }

        return true;
    }


    //o(nlogn)
    private boolean isStringsEqualI(String str1, String str2) {
        char[] chars1 = str1.toCharArray();
        Arrays.sort(chars1);
        String sortedStr1 = new String(chars1);
        char[] chars2 = str2.toCharArray();
        Arrays.sort(chars2);
        String sortedStr12 = new String(chars2);

        return sortedStr1.equals(sortedStr12);
    }

    public static void main(String[] args) {
        ScrambleString scrambleString = new ScrambleString();
        System.out.println(scrambleString.isScramble("sqksrqzhhmfmlmqvlbnaqcmebbkqfy", "abbkyfqemcqnblvqmlmfmhhzqrskqs"));
    }
}
