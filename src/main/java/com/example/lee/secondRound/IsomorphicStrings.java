package com.example.lee.secondRound;

import java.util.*;

/**
 * Created by benbendaisy on 4/28/15.
 *
 * Given two strings s and t, determine if they are isomorphic.
 *
 * Two strings are isomorphic if the characters in s can be replaced to get t.
 *
 * All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
 *
 * For example,
 * Given "egg", "add", return true.
 *
 * Given "foo", "bar", return false.
 *
 * Given "paper", "title", return true.
 */
public class IsomorphicStrings {
    private class ICharacter {
        private char ch;
        private int cnt;
        private ICharacter(char c, int count) {
            ch = c;
            cnt = count;
        }
    }

    public boolean isIsomorphic(String s, String t) {
        if (null == s && null == t) {
            return true;
        } else if (null == s || null == t || s.length() != t.length()) {
            return false;
        }
        List<ICharacter> list1 = new ArrayList<ICharacter>();
        List<ICharacter> list2 = new ArrayList<ICharacter>();
        morphic(s, list1);
        morphic(t, list2);
        Map<Character, Character> map = new HashMap<Character, Character>();
        Set<Character> set = new HashSet<Character>();
        for (int j = 0; j < list1.size(); j++) {
            if (list1.get(j).cnt != list2.get(j).cnt) return false;
            if (!map.containsKey(list1.get(j).ch) && set.contains(list2.get(j).ch)) return false;
            if (map.containsKey(list1.get(j).ch) && map.get(list1.get(j).ch) != list2.get(j).ch) return false;
            map.put(list1.get(j).ch, list2.get(j).ch);
            set.add(list2.get(j).ch);
        }

        return true;
    }

    private void morphic(String s, List<ICharacter> list) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        char[] chars = s.toCharArray();
        for (char ch : chars) {
            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
            }
            ICharacter ic = new ICharacter(ch, map.get(ch));
            list.add(ic);
        }
    }

    //this solution is not working
    public boolean isIsomorphicI(String s, String t) {
        if (null == s && null == t) {
            return true;
        } else if (null == s || null == t || s.length() != t.length()) {
            return false;
        }
        for (int i = 1; i < s.length(); i++) {
            Map<Character, Integer> map1 = new LinkedHashMap<Character, Integer>();
            Map<Character, Integer> map2 = new LinkedHashMap<Character, Integer>();
            String str1 = s.substring(0, i);
            String str2 = t.substring(0, i);
            morphic(str1, map1);
            morphic(str2, map2);
            if (map1.size() != map2.size()) return false;
            List<Integer> list1 = new ArrayList<Integer>(map1.values());
            List<Integer> list2 = new ArrayList<Integer>(map2.values());
            for (int j = 0; j < list1.size(); j++) {
                if (list1.get(j) != list2.get(j)) return false;
            }
        }

        return true;
    }

    private void morphic(String s, Map<Character, Integer> map) {
        char[] chars = s.toCharArray();
        for (char ch : chars) {
            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
            }
        }
    }

    public static void main(String[] args) {
        IsomorphicStrings isomorphicStrings = new IsomorphicStrings();
        System.out.println(isomorphicStrings.isIsomorphicI("aba", "baa"));
    }

}
