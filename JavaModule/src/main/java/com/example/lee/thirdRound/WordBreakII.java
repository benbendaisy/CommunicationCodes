package com.example.lee.thirdRound;

import java.util.*;
import java.util.stream.IntStream;

public class WordBreakII {
    /**
     * recursive way + memoinization
     * @param s
     * @param wordDict
     * @return
     */
    public List<String> wordBreak(String s, List<String> wordDict) {
        if (s == null || s.length() == 0) {
            return Collections.emptyList();
        }
        Set<String> dict = new HashSet<>(wordDict);
        return wordBreakHelper(s, dict, new HashMap<>());
    }
    private List<String> wordBreakHelper(String s, Set<String> dict, Map<String, List<String>> cached) {
        if (cached.containsKey(s)) {
            return cached.get(s);
        }
        if (s.isEmpty()) {
            return new ArrayList<>(Arrays.asList(""));
        }
        List<String> list = new ArrayList<>();
        for (int i = 1; i <= s.length(); i++) {
            String subString = s.substring(0, i);
            if (dict.contains(subString)) {
                String leftString = s.substring(i);
                List<String> stringList = wordBreakHelper(leftString, dict, cached);
                if (!stringList.isEmpty()) {
                    for (String str : stringList) {
                        StringBuilder sb = new StringBuilder();
                        sb.append(subString);
                        if (i != s.length()) {
                            // 如果左边为空，或是右边为空，不需要贴空格
                            sb.append(" ");
                        }
                        sb.append(str);
                        list.add(sb.toString());
                    }
                }
            }
        }
        cached.put(s, list);
        return list;
    }

    /**
     * dynamic solution but not pass leetcode because time limit exceeded
     * @param s
     * @param wordDict
     * @return
     */
    public List<String> wordBreakII(String s, List<String> wordDict) {
        if (s == null || s.length() == 0) {
            return Collections.emptyList();
        }
        Set<String> dict = new HashSet<>(wordDict);
        Set<Integer>[] indexSet = new Set[s.length() + 1];
        IntStream.range(0, indexSet.length).forEach(index -> indexSet[index] = new HashSet<>());
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                String subString = s.substring(j, i);
                if (dict.contains(subString)) {
                    indexSet[i].add(j);
                }
            }
        }
        List<String> res = new ArrayList<>();
        wordBreakResultGenerator(s, indexSet, s.length(), new ArrayList<>(), res);
        return res;
    }

    private void wordBreakResultGenerator(String str, Set<Integer>[] indexSet, int idx, List<String> candidates, List<String> res) {
        if (idx == 0) {
            res.add(String.join(" ", candidates));
            return;
        }
        for (int prev : indexSet[idx]) {
            List<String> newCandidates = new ArrayList<>(candidates);
            newCandidates.add(0, str.substring(prev, idx));
            wordBreakResultGenerator(str, indexSet, prev, newCandidates, res);
        }
    }
    /**
     * recursive way but not pass leetcode because of time limited
     * @param s
     * @param wordDict
     * @return
     */
    public List<String> wordBreakI(String s, List<String> wordDict) {
        if (s == null || s.length() == 0 || wordDict == null || wordDict.isEmpty()) {
            return Collections.emptyList();
        }
        Set<String> dict = new HashSet<>(wordDict);
        List<String> res = new ArrayList<>();
        wordBreakHelper(s, dict, new ArrayList<>(), 0, res);
        return res;
    }
    private void wordBreakHelper(String s, Set<String> dict, List<String> candidates, int idx, List<String> res) {
        if (idx == s.length()) {
            res.add(String.join(" ", candidates));
            return;
        }
        for (int i = idx + 1; i <= s.length(); i++) {
            String subStr = s.substring(idx, i);
            if (dict.contains(subStr)) {
                List<String> newCandidates = new ArrayList<>(candidates);
                newCandidates.add(subStr);
                wordBreakHelper(s, dict, newCandidates, i, res);
            }
        }
    }

    public static void main(String[] args) {
        WordBreakII wordBreakII = new WordBreakII();
        List<String> dict = Arrays.asList("a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa");
        String str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        wordBreakII.wordBreakII(str, dict).stream().forEach(System.out::println);
    }
}
