package com.example.lee.secondRound;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 4/7/15.
 * Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
 *
 * For example,
 * Given [100, 4, 200, 1, 3, 2],
 * The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
 *
 * Your algorithm should run in O(n) complexity.
 */
public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] num) {
        if (null == num) return 0;
        if (num.length <= 1) return num.length;
        Set<Integer> set = new HashSet<Integer>();
        for (int e : num) {
            set.add(e);
        }
        int max = 0;
        for (int e : num) {
            if (set.contains(e)) {
                int l = e - 1;
                int r = e + 1;
                int cnt = 1;
                set.remove(e);
                while (set.contains(l)) {
                    cnt++;
                    set.remove(l);
                    l--;
                }
                while (set.contains(r)) {
                    cnt++;
                    set.remove(r);
                    r++;
                }
                max = Math.max(max, cnt);
            }
        }
        return max;
    }
}
