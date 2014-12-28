package com.example.lee;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Created by benbendaisy on 12/27/14.
 *
 * Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
 * For example,
 * Given [100, 4, 200, 1, 3, 2],
 * The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
 * Your algorithm should run in O(n) complexity.
 */
public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] num) {
        if(num == null || num.length == 0){
            return 0;
        } else if(num.length == 1){
            return 1;
        }

        int len = num.length;
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < len; i++){
            set.add(num[i]);
        }
        int max = 0;
        for(int e : num){
            int left = e - 1;
            int right = e + 1;
            int count = 1;
            set.remove(e);
            while(set.contains(left)){
                count++;
                set.remove(left);
                left--;
            }
            while(set.contains(right)){
                count++;
                set.remove(right);
                right++;
            }
            max = Math.max(max, count);
        }
        return max;
    }

    public static void main(String[] args) {
        LongestConsecutiveSequence longestConsecutiveSequence = new LongestConsecutiveSequence();
        int[] num = {1,0,-1};
        //System.out.println(longestConsecutiveSequence.longestConsecutive(num));

        Set<String> set = new HashSet<String>();
        set.add("A");
        set.add("B");

        for (String s : set) {
            if (s.equals("B")) {
                set.remove(s);
            }
        }
    }
}
