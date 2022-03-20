package com.example.lee.thirdRound;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class ScrambleString {

    public boolean isScramble(String s1, String s2) {
        if (s1 == null && s2 == null) {
            return true;
        } else if (s1 == null || s2 == null) {
            return false;
        } else if (s1.length() != s2.length()) {
            return false;
        } else if (s1.length() == 0 || s1.equals(s2)) {
            return true;
        }

        if (!canBeScramble(s1, s2)) {
            return false;
        }

        for (int i = 1; i < s1.length(); i++) {
            String s11 = s1.substring(0, i);
            String s12 = s1.substring(i);
            String s21 = s2.substring(0, i);
            String s22 = s2.substring(i);
            String s23 = s2.substring(s2.length() - i);
            String s24 = s2.substring(0, s2.length() - i);
            if ((isScramble(s11, s21) && isScramble(s12, s22))
                    || (isScramble(s11, s23) && isScramble(s12, s24))) {
                return true;
            }
        }
        return false;
    }

    private boolean canBeScramble(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return false;
        }
        Map<Character, Integer> strMap = IntStream.range(0, s1.length())
                .boxed()
                .map(idx -> Character.valueOf(s1.charAt(idx)))
                .collect(Collectors.toMap(Function.identity(), ch -> 1, (a, b) -> a + b));

        for (int i = 0; i < s2.length(); i++) {
            Character ch = s2.charAt(i);
            if (!strMap.containsKey(ch) || strMap.get(ch) < 1) {
                return false;
            }
            strMap.put(ch, strMap.get(ch) - 1);
        }

        return true;
    }

    public boolean isScrambleI(String s1, String s2) {
        if (s1 == null && s2 == null) {
            return true;
        } else if (s1 == null || s2 == null) {
            return false;
        } else if (s1.length() != s2.length()) {
            return false;
        } else if (s1.length() == 0) {
            return true;
        }
        Map<String, Map<String, Boolean>> cached = new HashMap<>();
        return isScramble(s1, s2, cached);
    }

    private boolean isScramble(String s1, String s2, Map<String, Map<String, Boolean>> cached) {
        if (s1.length() != s2.length()) {
            return false;
        } else if (s1.length() == 0) {
            return true;
        }
        if (cached.containsKey(s1) && cached.get(s1).containsKey(s2)) {
            return cached.get(s1).get(s2);
        } else if (s1.equals(s2)) {
            return true;
        }
        for (int i = 1; i < s1.length(); i++) {
            String s11 = s1.substring(0, i);
            String s12 = s1.substring(i);
            String s21 = s2.substring(0, i);
            String s22 = s2.substring(i);
            String s23 = s2.substring(s2.length() - i);
            String s24 = s2.substring(0, s2.length() - i);
            if ((isScramble(s11, s21) && isScramble(s12, s22))
                    || (isScramble(s11, s23) && isScramble(s12, s24))) {
                return true;
            }
        }
        Map<String, Boolean> map = cached.getOrDefault(s1, new HashMap<>());
        map.put(s2, false);
        cached.put(s1, map);
        return false;
    }

    public static void main(String[] args) {
        ScrambleString scrambleString = new ScrambleString();
        System.out.println(scrambleString.isScramble("a","a"));
    }
}
