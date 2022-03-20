package com.example.lee.thirdRound;

import java.util.*;

public class WordLadder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (beginWord == null || endWord == null || beginWord.length() != endWord.length() || beginWord.equals(endWord)) {
            return 0;
        }
        Queue<String> queue = new LinkedList<>();
        Queue<Integer> queueLevel = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        Set<String> dict = new HashSet<>(wordList);
        queue.add(beginWord);
        queueLevel.add(1);
        while (!queue.isEmpty()) {
            String str = queue.poll();
            visited.add(str);
            int level = queueLevel.poll();
            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                char[] words = str.toCharArray();
                for (char j = 'a'; j <= 'z'; j++) {
                    words[i] = j;
                    if (ch != j) {
                        String temp = new String(words);
                        if (!dict.contains(temp)) {
                            continue;
                        } else if (endWord.equals(temp)) {
                            return level + 1;
                        } else if (visited.add(temp)) {
                            queue.add(temp);
                            queueLevel.add(level + 1);
                        }
                    }
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        WordLadder wordLadder = new WordLadder();
        List<String> wordList = Arrays.asList("hot","dot","dog","lot","log","cog");
        System.out.println(wordLadder.ladderLength("hit", "cog", wordList));
    }
}
