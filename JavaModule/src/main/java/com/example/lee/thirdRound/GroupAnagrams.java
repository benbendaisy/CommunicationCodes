package com.example.lee.thirdRound;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * Created by benbendaisy on 7/8/17.
 */
public class GroupAnagrams {
    /**
     * it passed leetcode but reach 0.10%
     * @param strs
     * @return
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) {
            return Collections.emptyList();
        }
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            String sortedStr = sortedString(s);
            List<String> list = map.getOrDefault(sortedStr, new ArrayList<>());
            list.add(s);
            map.put(sortedStr, list);
        }
        return map.values().stream().collect(Collectors.toList());
    }

    /**
     * both passed leetcode but it seems streaming features in java 8 is slow
     * @param strs
     * @return
     */
    public List<List<String>> groupAnagramsI(String[] strs) {
        if (strs == null || strs.length == 0) {
            return Collections.emptyList();
        }
        Map<String, List<String>> stringListMap = Arrays.stream(strs)
                .collect(Collectors.groupingBy(this::sortedString));
        return stringListMap.values().stream().collect(Collectors.toList());
    }

    private String sortedString(String str) {
        return str.chars()
                .mapToObj(i -> (char) i)
                .sorted()
                .collect(Collectors.toList())
                .toString();
    }

    public static void main(String[] args) {
        GroupAnagrams groupAnagrams = new GroupAnagrams();
        System.out.println(groupAnagrams.sortedString("ate"));
    }
}
