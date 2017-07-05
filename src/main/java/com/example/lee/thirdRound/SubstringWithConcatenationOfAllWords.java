package com.example.lee.thirdRound;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Created by benbendaisy on 7/4/17.
 *
 * You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
 *
 * For example, given:
 * s: "barfoothefoobarman"
 * words: ["foo", "bar"]
 *
 * You should return the indices: [0,9].
 * (order does not matter).
 */
public class SubstringWithConcatenationOfAllWords {
    public List<Integer> findSubstring(String s, String[] words) {
        if (s == null || words == null || words.length == 0 || words[0].length() == 0) {
            return Collections.emptyList();
        }
        int len = words[0].length();
        Map<String, Integer> tMap = Stream.of(words)
                .collect(Collectors.toMap(Function.identity(), i -> 1, (a, b) -> a + b));

        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            Map<String, Integer> curMap = new HashMap<>();
            int count = 0;
            int left = i;
            for (int j = i; j <= s.length() - len; j += len) {
                String str = s.substring(j, j + len);
                if (tMap.containsKey(str)) {
                    curMap.put(str, curMap.getOrDefault(str, 0) + 1);
                    if (curMap.get(str) <= tMap.get(str)) {
                        count++;
                    } else {
                        while (curMap.get(str) > tMap.get(str)) {
                            String string = s.substring(left, left + len);
                            curMap.put(string, curMap.get(string) - 1);
                            if (curMap.get(string) < tMap.get(string)) {
                                count--;
                            }
                            left += len;
                        }
                    }
                    if (count == words.length) {
                        res.add(left);
                        String temp = s.substring(left, left + len);
                        curMap.put(temp, curMap.get(temp) - 1);
                        count--;
                        left = left + len;
                    }
                } else {
                    curMap.clear();
                    count = 0;
                    left = j + len;
                }
            }
        }
        return res;
    }

    public List<Integer> findSubstringI(String s, String[] words) {
        if (s == null || words == null || words.length == 0) {
            return Collections.emptyList();
        }
        List<Integer> res = new ArrayList<>();
        Map<String, Integer> tMap =
                Stream.of(words).collect(Collectors.toMap(Function.identity(), i -> 1, (a, b) -> a + b));
        int len = words[0].length();
        for (int i = 0; i < len; i++) {
            Map<String, Integer> curMap = new HashMap<>();
            int left = i;
            int count = 0;
            for (int j = i; j <= s.length() - len; j += len) {
                String str = s.substring(j, j + len);
                if (tMap.containsKey(str)) {
                    curMap.put(str, curMap.getOrDefault(str, 0) + 1);
                    if (curMap.get(str) <= tMap.get(str)) {
                        count++;
                    }
                    // squeeze the word
                    while (tMap.get(str) < curMap.get(str)) {
                        String string = s.substring(left, left + len);
                        curMap.put(string, curMap.get(string) - 1);
                        if (curMap.get(string) < tMap.get(string)) {
                            count--;
                        }
                        left += len;
                    }

                    if (count == words.length) {
                        res.add(left);
                        String temp = s.substring(left, left + len);
                        curMap.put(temp, curMap.get(temp) - 1);
                        count--;
                        left += len;
                    }
                } else {
                    curMap.clear();
                    left = j + len;
                    count = 0;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        SubstringWithConcatenationOfAllWords substringWithConcatenationOfAllWords = new SubstringWithConcatenationOfAllWords();
        String[] words = {"foo","bar"};
        System.out.println(substringWithConcatenationOfAllWords.findSubstring("barfoothefoobarman", words));
    }
}
