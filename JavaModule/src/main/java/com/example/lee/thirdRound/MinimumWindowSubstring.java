package com.example.lee.thirdRound;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Created by benbendaisy on 7/15/17.
 */
public class MinimumWindowSubstring {
    public String minWindow(String s, String t) {
        if (s == null || t == null || t.length() == 0) {
            return "";
        }

        char[] patternCharacters = t.toCharArray();
        Map<Character, Integer> patternMap = IntStream.range(0, patternCharacters.length)
                .mapToObj(i -> patternCharacters[i])
                .collect(Collectors.toMap(Function.identity(), i -> 1, (a, b) -> a + b));
        int curLen = 0;
        int left = 0;
        int minStart = 0;
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (!patternMap.containsKey(ch)) {
                continue;
            }
            patternMap.put(ch, patternMap.get(ch) - 1);
            if (patternMap.get(ch) >= 0) {
                curLen++;
            }
            if (curLen >= t.length()) {
                while (left <= i && (!patternMap.containsKey(s.charAt(left))) || patternMap.get(s.charAt(left)) < 0) {
                    if (patternMap.containsKey(s.charAt(left))) {
                        patternMap.put(s.charAt(left), patternMap.get(s.charAt(left)) + 1);
                        if (patternMap.get(s.charAt(left)) > 0) {
                            curLen--;
                        }
                    }
                    left++;
                }
                if (minLen > i - left + 1) {
                    minLen = i - left + 1;
                    minStart = left;
                }
            }
        }
        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
    }

    public static void main(String[] args) {
        MinimumWindowSubstring minimumWindowSubstring = new MinimumWindowSubstring();
        System.out.println(minimumWindowSubstring.minWindow("bbaac", "aba"));
    }
}
