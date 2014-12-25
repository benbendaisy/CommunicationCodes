package com.example.lee;

import java.util.*;

/**
 * Created by benbendaisy on 12/23/14.
 * Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
 * Return all such possible sentences.
 * For example, given
 * s = "catsanddog",
 * dict = ["cat", "cats", "and", "sand", "dog"].
 * A solution is ["cats and dog", "cat sand dog"].
 */
public class WordBreakII {
//    public List<String> wordBreakI(String s, Set<String> dict) {
//        Set<String> cand = new HashSet<String>();
//        Set<String> result = new HashSet<String>();
//        Map<String, List<Set<String>>> map = new HashMap<String, List<Set<String>>>();
//        wordBreakHelp(s, dict, cand, map, result);
//        return new ArrayList<String>(result);
//    }
//
//    private boolean wordBreakHelp(String s, Set<String> dict, Set<String> cand, Map<String, List<Set<String>>> map, Set<String> result){
//        boolean canBeBroken = false;
//        if(s == null || s.isEmpty()){
//            return true;
//        }
//
//        if (map.containsKey(s) && null != map.get(s)){
//            for(Set<String> ls : map.get(s)){
//                List<String> cands = new ArrayList<String>();
//                cands.addAll(cand);
//                cands.addAll(ls);
//                String str = listToString(cands);
//                result.add(str);
//            }
//            canBeBroken = true;
//        } else if(!map.containsKey(s)){
//            for(int i = 1; i <= s.length(); i++){
//                String subStr = s.substring(0, i);
//                if(dict.contains(subStr)){
//                    Set<String> candidate = new HashSet<String>();
//                    candidate.addAll(cand);
//                    candidate.add(subStr);
//                    if(wordBreakHelp(s.substring(i), dict, candidate, map, result)){
//                        candidate.removeAll(cand);
//                        if(map.containsKey(s)){
//                            map.get(s).add(candidate);
//                        } else {
//                            List<Set<String>> lists = new ArrayList<Set<String>>();
//                            lists.add(candidate);
//                            map.put(s, lists);
//                        }
//                    }
//                }
//            }
//        }
//
//        if (dict.contains(s)){
//            //cand.add(s);
//            Set<String> set = new HashSet<String>();
//            set.add(s);
//            if(map.containsKey(s)){
//                for(Set<String> ss : map.get(s)){
//                    ss.add(s);
//                }
//                map.get(s).add(set);
//            } else {
//                List<Set<String>> lss = new ArrayList<Set<String>>();
//                lss.add(set);
//                map.put(s, lss);
//            }
//            for(Set<String> ss : map.get(s)){
//                List<String> cands = new ArrayList<String>();
//                cands.addAll(cand);
//                cands.addAll(ss);
//                String str = listToString(cands);
//                result.add(str);
//            }
//            //cand.clear();
//            canBeBroken = true;
//        }
//
//        if(!map.containsKey(s)){
//            map.put(s, null);
//        }
//
//        return canBeBroken;
//    }
//
//    private String listToString(List<String> list){
//        StringBuilder sb = new StringBuilder();
//        if(list != null && list.size() > 0){
//            for(String str : list){
//                sb.append(str);
//                sb.append(" ");
//            }
//            sb.deleteCharAt(sb.length() - 1);
//            return sb.toString();
//        }
//        return null;
//    }


    public List<String> wordBreak(String s, Set<String> dict) {
        List<String> resultList = new ArrayList<String>();
        if(s == null || s.isEmpty()){
            return resultList;
        }
        int len = s.length();
        boolean canBeBroken = false;
        Map<Integer, Set<Integer>> wb = new HashMap<Integer, Set<Integer>>();
        for(int i = 1; i <= len; i++){
            String subStr1 = s.substring(0, i);
            if(dict.contains(subStr1) || wb.containsKey(i)){
                if(dict.contains(subStr1)){
                    if(wb.containsKey(i)){
                        wb.get(i).add(0);
                    } else {
                        Set<Integer> set = new HashSet<Integer>();
                        set.add(0);
                        wb.put(i, set);
                    }
                    if(i == len){
                        canBeBroken = true;
                    }
                }
                for(int j = i+1; j <= len; j++){
                    String subStr2 = s.substring(i, j);
                    if(dict.contains(subStr2)){
                        if(j == len){
                            canBeBroken = true;
                        }
                        if(wb.containsKey(j)){
                            wb.get(j).add(i);
                        } else {
                            Set<Integer> set = new HashSet<Integer>();
                            set.add(i);
                            wb.put(j, set);
                        }
                    }
                }
            }
        }
        if(canBeBroken){
            getSegmentString(s, wb, s.length(), "", resultList);
        }

        return resultList;
    }

    private void getSegmentString(String input, Map<Integer, Set<Integer>> wb, int index, String resultStr, List<String> list){
        if(input == null || input.isEmpty() || wb == null || wb.size() == 0){
            return;
        }
        if(index != 0){
            if(!wb.containsKey(index)){
                resultStr = input.substring(0, index) + " " + resultStr;
                index = 0;
                getSegmentString(input, wb, index, resultStr, list);
            } else {
                Set<Integer> set = wb.get(index);
                for(int element : set){
                    String tempStr = input.substring(element, index) + " " + resultStr;
                    getSegmentString(input, wb, element, tempStr, list);
                }
            }
        } else {
            list.add(resultStr.trim());
        }
    }

    public static void main(String[] args) {
        WordBreakII wb = new WordBreakII();
        //String[] strArray = new String[]{"abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"};
        //Set<String> dict = new HashSet<String>(Arrays.asList("a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"));
        Set<String> dict = new HashSet<String>(Arrays.asList("aaaa","aa","a"));
        Map<String, String> memoized = new HashMap<String, String>();
        //dict.add("a");

        System.out.println(wb.wordBreak("aaaa", dict));
    }
}

