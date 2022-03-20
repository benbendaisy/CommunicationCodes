package com.example.lee.firstRound;

import java.util.*;

/**
 * Created by benbendaisy on 12/27/14.
 * Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
 * Only one letter can be changed at a time
 * Each intermediate word must exist in the dictionary
 * For example,
 * Given:
 * start = "hit"
 * end = "cog"
 * dict = ["hot","dot","dog","lot","log"]
 * As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * return its length 5.
 * Note:
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 */
public class WordLadder {
    public int ladderLength(String start, String end, Set<String> dict) {
        if(start == null || end == null || start.length() != end.length() ){
            return 0;
        }
        Queue<String> queue = new LinkedList<String>();
        Queue<Integer> queueLevel = new LinkedList<Integer>();
        Set<String> visited = new HashSet<String>();

        int len = start.length();
        queue.add(start);
        queueLevel.add(1);
        while(!queue.isEmpty()){
            String str = queue.poll();
            int level = queueLevel.poll();
            visited.add(str);
            for(int i = 0; i < len; i++){
                char[] word = str.toCharArray();
                for(char c = 'a'; c <= 'z'; c++){
                    word[i] = c;
                    String tempStr = new String(word);
                    if (dict.contains(tempStr)) {
                        if (end.equals(tempStr)) {
                            return level + 1;
                        } else if (visited.add(tempStr)) {
                            queue.add(tempStr);
                            queueLevel.add(level + 1);
                        }
                    }

                }
            }
        }
        return 0;
    }

    //remove the queue that saves levels
    public int ladderLengthI(String start, String end, Set<String> dict) {
        if(start == null || end == null || start.length() != end.length() ){
            return 0;
        }
        Queue<String> queue = new LinkedList<String>();
        Set<String> visited = new HashSet<String>();

        int len = start.length();
        queue.add(start);
        int level = 1;
        int preCount = 1;
        int currentCount = 0;
        while(!queue.isEmpty()){
            String str = queue.poll();
            preCount--;
            visited.add(str);
            for(int i = 0; i < len; i++){
                char[] word = str.toCharArray();
                for(char c = 'a'; c <= 'z'; c++){
                    word[i] = c;
                    String tempStr = new String(word);
                    if(end.equals(tempStr)){
                        return level + 1;
                    }
                    if(dict.contains(tempStr) && visited.add(tempStr)){
                        currentCount++;
                        queue.add(tempStr);
                    }
                }
            }
            if(preCount == 0){
                preCount = currentCount;
                currentCount = 0;
                level++;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        WordLadder wl = new WordLadder();
        Set<String> set = new HashSet<String>(Arrays.asList("hot","dog", "dot"));
        System.out.println(wl.ladderLength("hot", "dog", set));
    }
}
