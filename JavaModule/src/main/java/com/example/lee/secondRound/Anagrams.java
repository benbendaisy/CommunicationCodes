package com.example.lee.secondRound;

import java.util.*;

/**
 * Created by benbendaisy on 6/22/15.
 *
 * Given an array of strings, return all groups of strings that are anagrams.
 */
public class Anagrams {
    public List<String> anagrams(String[] strs) {
        List<String> list = new ArrayList<>();
        if (null == strs && strs.length < 1) return list;
        Map<String, Set<String>> map = new HashMap<>();
        for (String str : strs) {
            String key = getKey(str);
            if (!map.containsKey(key)) map.put(key, new HashSet<>());
            map.get(key).add(str);
        }
        for (String key : map.keySet()) {
            if (map.get(key).size() > 1) list.addAll(map.get(key));
        }
        return list;
    }

    private String getKey(String str) {
        int[] arry = new int[52];
        for (char ch : str.toCharArray()) {
            arry[ch - 'a']++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 52; i++) {
            if (arry[i] != 0) {
                char ch = (char) (i + 'a');
                sb.append(ch + arry[i]);
            }
        }
        return sb.toString();
    }
}
