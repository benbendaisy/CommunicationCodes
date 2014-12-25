package com.example.lee;

import java.util.*;

/**
 * Created by benbendaisy on 12/23/14.
 * Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
 * For example, given
 * s = "leetcode",
 * dict = ["leet", "code"].
 * Return true because "leetcode" can be segmented as "leet code".
 */
public class WordBreak {

    //recursive with memoi
    public boolean wordBreak(String s, Set<String> dict) {
        Map<String, Boolean> map = new HashMap<String, Boolean>();
        return SegmentString(s, dict, map);
    }

    private Boolean SegmentString(String input, Set<String> dict, Map<String, Boolean> memoized){
        if (input == null || input.isEmpty() || dict.contains(input)) {
            return true;
        } else if(memoized.containsKey(input)){
            return memoized.get(input);
        }
        int len = input.length();
        for (int i = 1; i < len; i++) {
            String prefix = input.substring(0, i);
            if (dict.contains(prefix)) {
                String suffix = input.substring(i, len);
                boolean segSuffix = SegmentString(suffix, dict, memoized);
                if (segSuffix) {
                    memoized.put(input, true);
                    return true;
                }
            }
        }
        memoized.put(input, false);
        return false;
    }

    //dynamic programming way
    public boolean wordBreak1(String s, Set<String> dict) {
        if(s == null || s.isEmpty()){
            return false;
        }
        int len = s.length();
        boolean[] wb = new boolean[len + 1];

        for(int i = 1; i <= len; i++){
            String subStr1 = s.substring(0, i);
            if(dict.contains(subStr1) && !wb[i]){
                wb[i] = true;
            }
            if(wb[i]){
                if(i == len){
                    return true;
                }
                for(int j = i+1; j <= len; j++){
                    String subStr2 = s.substring(i, j);
                    if(dict.contains(subStr2) && !wb[j]){
                        wb[j] = true;
                    }
                    if(j == len && wb[j]){
                        return true;
                    }
                }
            }

        }
        return false;
    }

    public static void main(String[] args) {
        WordBreak wb = new WordBreak();
        //String[] strArray = new String[]{"abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"};
//        Set<String> dict = new HashSet<String>(Arrays.asList("abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"));
        Set<String> dict = new HashSet<String>(Arrays.asList("a","abc","b","cd"));
        //dict.add("a");
//        System.out.println(wb.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", dict));
        System.out.println(wb.wordBreak1("abcd", dict));
        StringBuffer sb = new StringBuffer();
        sb.deleteCharAt(sb.length());
    }
}
