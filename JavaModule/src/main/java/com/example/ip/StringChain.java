package com.example.ip;

import java.util.*;

/**
 * Created by benbendaisy on 4/28/15.
 */
public class StringChain {
    //this solution passed tests
    static int longest_chain(String[] w) {
        if (null == w || w.length == 0) return 0;
        Set<String> dict = new HashSet<String>();
        for (String word : w) {
            dict.add(word);
        }
        int max = 0;
        for (String word : w) {
            Queue<String> queue1 = new LinkedList<String>();
            Queue<Integer> queue2 = new LinkedList<Integer>();
            int level = 1;
            queue1.add(word);
            queue2.add(level);
            Map<String, Integer> visited = new HashMap<String, Integer>();
            int lMax = 0;
            while (!queue1.isEmpty()) {
                String str = queue1.poll();
                level = queue2.poll();
                lMax = Math.max(lMax, level);
                String newStr = str.substring(1);
                if (dict.contains(newStr) && !visited.containsKey(newStr)) {
                    queue1.add(newStr);
                    queue2.add(level + 1);
                    visited.put(newStr, level);
                }
                for (int i = 1; i < str.length(); i++) {
                    newStr = removeIthCharacter(str, i);
                    if (dict.contains(newStr) && !visited.containsKey(newStr)) {
                        queue1.add(newStr);
                        queue2.add(level + 1);
                        visited.put(newStr, level);
                    }
                }
            }
            max = Math.max(max, lMax);
        }
        return max;
    }

    //did not pass tests as there are some issues that calculate maximal length
    static int longest_chainI(String[] w) {
        if (null == w || w.length == 0) return 0;
        Set<String> dict = new HashSet<String>();
        for (String word : w) {
            dict.add(word);
        }
        int max = 0;
        Map<String, Integer> visited = new HashMap<String, Integer>();
        for (String word : w) {
            Queue<String> queue1 = new LinkedList<String>();
            Queue<Integer> queue2 = new LinkedList<Integer>();
            int level = 1;
            queue1.add(word);
            queue2.add(level);
            Map<String, Set<String>> map = new HashMap<String, Set<String>>();
            int lMax = 0;
            while (!queue1.isEmpty()) {
                String str = queue1.poll();
                level = queue2.poll();
                lMax = Math.max(lMax, level);
                String newStr = str.substring(1);
                if (visited.containsKey(newStr)) {
                    lMax = Math.max(lMax, level + visited.get(newStr));
                } else if (dict.contains(newStr)) {
                    if (map.containsKey(str)) {
                        map.get(str).add(newStr);
                    } else {
                        Set<String> set = new HashSet<String>();
                        set.add(newStr);
                        map.put(str, set);
                    }
                    queue1.add(newStr);
                    queue2.add(level + 1);
                }

                for (int i = 1; i < str.length(); i++) {
                    newStr = removeIthCharacter(str, i);
                    if (visited.containsKey(newStr)) {
                        max = Math.max(max, level + visited.get(newStr));
                    } else if (dict.contains(newStr)) {
                        queue1.add(newStr);
                        queue2.add(level + 1);
                        if (map.containsKey(str)) {
                            map.get(str).add(newStr);
                        } else {
                            Set<String> set = new HashSet<String>();
                            set.add(newStr);
                            map.put(str, set);
                        }
                        visited.put(newStr, level);
                    }
                }
            }
            for (String str : map.keySet()) {
                if (!visited.containsKey(str)) {
                    int left = getLongestPath(map, str, 0);
                    visited.put(str, left);
                }
            }
            max = Math.max(max, lMax);
        }
        return max;
    }

    private static String removeIthCharacter(String str, int idx) {
        String newStr = str.substring(0, idx) + str.substring(idx + 1, str.length());
        return newStr;
    }

    //there is some problems here
    private static int getLongestPath(Map<String, Set<String>> map, String str, int level) {
        Set<String> set = map.get(str);
        int max = Math.max(0, level);
        if (null != set) {
            for (String string : set) {
                if (map.containsKey(string)) {
                    max = Math.max(max, getLongestPath(map, string, level + 1));
                }
            }
        }
        return max;
    }
}
