package com.example.lee.firstRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 3/14/15.
 *
 * Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb".
 * refers to: http://www.danielbit.com/blog/puzzle/leetcode/leetcode-longest-substring-with-at-most-two-distinct-characters
 */
public class LongestSubstringWhichContains2UniqueCharacters {

    //sliding window
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (null == s || s.length() < 1) {
            return 0;
        }
        int l = 0, r = -1;
        int max = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                continue;
            } else if (r != -1 && s.charAt(i) != s.charAt(r)) {
                max = Math.max(i - l, max);
                l = r + 1;
            }
            r = i - 1;
        }
        return Math.max(s.length() - l, max);
    }

    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (null == s || s.length() < k) {
            return 0;
        }

        Map<Character, Integer> map = new HashMap<Character, Integer>();
        int idx = 0, count = 0, max = 0, l = 0;

        while (idx < s.length()) {
            char ch = s.charAt(idx);
            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
                count++;
                max = Math.max(max, idx - l);
                while (l < idx && count > k) {
                    char c = s.charAt(l);
                    if (map.get(c) == 1) {
                        map.remove(c);
                        count--;
                        l++;
                        break;
                    } else {
                        map.put(c, map.get(c) - 1);
                    }
                    l++;
                }
            }
            idx++;
        }
        return Math.max(max, s.length() - l);
    }

    public static void main(String[] args) {
        LongestSubstringWhichContains2UniqueCharacters longestSubstringWhichContains2UniqueCharacters = new LongestSubstringWhichContains2UniqueCharacters();
        System.out.println(longestSubstringWhichContains2UniqueCharacters.lengthOfLongestSubstringKDistinct("babaadadd", 2));
    }

}
