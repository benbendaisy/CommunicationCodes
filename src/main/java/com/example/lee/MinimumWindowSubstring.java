package com.example.lee;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 1/14/15.
 * Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
 *
 * For example,
 * S = "ADOBECODEBANC"
 * T = "ABC"
 * Minimum window is "BANC".
 *
 * Note:
 * If there is no such window in S that covers all characters in T, return the emtpy string "".
 *
 * If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
 */
public class MinimumWindowSubstring {
    public String minWindow(String S, String T) {
        if(S == null || T == null || S.length() < T.length()){
            return "";
        }

        Map<Character, Integer> map = new HashMap<Character, Integer>();
        //initial map
        for(int i = 0; i < T.length(); i++){
            char c = T.charAt(i);
            if(map.containsKey(c)){
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        int left = 0, minWin = S.length() + 1, minStart = 0, curLen = 0;
        for(int i = 0; i < S.length(); i++){
            char c = S.charAt(i);
            if(!map.containsKey(c)){
                continue;
            }
            map.put(c, map.get(c) - 1);

            //curLen is used to count how many valid characters in T are covered
            if(map.get(c) >= 0){
                curLen++;
            }
            //find a valid window
            while(curLen >= T.length()){
                //get window length and start
                if(i - left + 1 < minWin){
                    minWin = i - left + 1;
                    minStart = left;
                }
                //move the left of window
                char c1 = S.charAt(left);
                if(map.containsKey(c1)){
                    map.put(c1, map.get(c1) + 1);
                    //check if the window loose a valid character
                    if(map.get(c1) > 0){
                        curLen--;
                    }
                }
                left++;
            }
        }
        return minWin > S.length() ? "" : S.substring(minStart, minStart + minWin);
    }

    public static void main(String[] args) {
        MinimumWindowSubstring minimumWindowSubstring = new MinimumWindowSubstring();
        System.out.println(minimumWindowSubstring.minWindow("a", "a"));
    }
}
