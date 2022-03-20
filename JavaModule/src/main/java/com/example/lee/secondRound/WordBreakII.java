package com.example.lee.secondRound;

import java.util.*;

/**
 * Created by benbendaisy on 4/1/15.
 */
public class WordBreakII {
    public List<String> wordBreak(String s, Set<String> dict) {
        List<String> list = new ArrayList<String>();
        if (null == s) {
            return list;
        } else if (dict.contains(s)) {
            list.add(s);
            return list;
        }

        Map<Integer, Set<Integer>> wb = new HashMap<Integer, Set<Integer>>();
        int len = s.length();
        boolean canBeBroken = false;

        for (int i = 1; i <= len; i++) {
            String subStr = s.substring(0, i);
            if (dict.contains(subStr) || wb.containsKey(i)) {
                if (dict.contains(subStr)) {
                    Set<Integer> set = null;
                    if (wb.containsKey(i)) {
                        set = wb.get(i);
                    } else {
                        set = new HashSet<Integer>();
                        wb.put(i, set);
                    }
                    set.add(0);
                }
                if (i == len) canBeBroken = true;
                for (int j = i + 1; j <= len; j++) {
                    String str = s.substring(i, j);
                    if (dict.contains(str)) {
                        Set<Integer> set = null;
                        if (wb.containsKey(j)) {
                            set = wb.get(j);
                        } else {
                            set = new HashSet<Integer>();
                            wb.put(j, set);
                        }
                        set.add(i);
                        if (j == len) canBeBroken = true;
                    }
                }
            }
        }
        if (canBeBroken) {
            List<String> candidate = new ArrayList<String>();
            getBrokenWords(s, wb, list, s.length(), candidate);
        }
        return list;
    }

    private void getBrokenWords(String s, Map<Integer, Set<Integer>> wb, List<String> list, int idx, List<String> candidate) {
        if (idx == 0) {
            StringBuilder sb = new StringBuilder();
            for (int i = candidate.size() - 1; i >= 0; i--) {
                sb.append(candidate.get(i));
                sb.append(" ");
            }
            sb.deleteCharAt(sb.length() - 1);
            list.add(sb.toString());
            return;
        }
        if (wb.containsKey(idx)) {
            Set<Integer> set = wb.get(idx);
            for (int i : set) {
                candidate.add(s.substring(i, idx));
                getBrokenWords(s, wb, list, i, candidate);
                candidate.remove(candidate.size() - 1);
            }
        }
    }

    public static void main(String[] args) {
        WordBreakII wordBreakII = new WordBreakII();
        Set<String> dict = new HashSet<String>(Arrays.asList("a", "abc", "b", "cd"));
        System.out.println(wordBreakII.wordBreak("abcd", dict));
    }
}
