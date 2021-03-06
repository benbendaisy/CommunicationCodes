package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Created by benbendaisy on 6/19/17.
 */
public class LengthOfLongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        if (s == null || s.length() == 0) {
            return maxLength;
        }
        Map<Character, Integer> characterSeenMap = new HashMap<>();
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            if (characterSeenMap.containsKey(s.charAt(i)) && start <= characterSeenMap.get(s.charAt(i))) {
                start = characterSeenMap.get(s.charAt(i)) + 1;
            }
            if (maxLength < i - start + 1) {
                maxLength = i - start + 1;
            }
            characterSeenMap.put(s.charAt(i), i);
        }
        return Math.max(maxLength, s.length() - start);
    }


    public int lengthOfLongestSubstringI(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        } else if (s.length() == 1) {
            return 1;
        }
        Set<Character> seenSet = new HashSet<>();
        int walker = 0;
        int runner = 0;
        int maxLen = 0;
        while (runner < s.length()) {
            if (!seenSet.add(s.charAt(runner))) {
                if (maxLen < runner - walker) {
                    maxLen = runner - walker;
                }
                while (s.charAt(walker) != s.charAt(runner)) {
                    seenSet.remove(s.charAt(walker));
                    walker++;
                }
                walker++;
            }
            runner++;
        }
        return Math.max(maxLen, runner - walker);
    }

    public static void main(String[] args) {
        LengthOfLongestSubstring lengthOfLongestSubstring = new LengthOfLongestSubstring();
        int maxLength = lengthOfLongestSubstring.lengthOfLongestSubstring("abcabcbb");
        System.out.println(maxLength);
    }
}
