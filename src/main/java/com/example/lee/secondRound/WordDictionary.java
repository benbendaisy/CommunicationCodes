package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/17/15.
 */
public class WordDictionary {
    private class TrieNode {
        char ch;
        boolean isEnd;
        List<TrieNode> childWords;
        public TrieNode(char ch) {
            childWords = new ArrayList<TrieNode>();
            this.ch = ch;
        }

        public TrieNode getChild(char ch) {
            for (TrieNode node : childWords) {
                if (node.ch == ch) return node;
            }
            return null;
        }
    }

    private TrieNode root;
    public WordDictionary() {
        root = new TrieNode(' ');
    }

    // Adds a word into the data structure.
    public void addWord(String word) {
        char[] chars = word.toCharArray();
        TrieNode cur = root;
        for (char ch : chars) {
            TrieNode child = cur.getChild(ch);
            if (null == child) {
                child = new TrieNode(ch);
                cur.childWords.add(child);
            }
            cur = child;
        }
        cur.isEnd = true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        if (null == word) return false;
        if (word.length() == 0) return true;
        return search(word, root);
    }

    public boolean search(String word, TrieNode root) {
        char ch = word.charAt(0);
        if (word.length() == 1) {
            if (ch == '.') {
                for (TrieNode node : root.childWords) {
                    if (node.isEnd) return true;
                }
                return false;
            } else {
                TrieNode child = root.getChild(ch);
                if (null == child || !child.isEnd) return false;
                return true;
            }
        }
        if (ch != '.') {
            TrieNode child = root.getChild(ch);
            if (null == child) return false;
            return search(word.substring(1), child);
        } else {
            for (TrieNode node : root.childWords) {
                if (search(word.substring(1), node)) return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        WordDictionary wd = new WordDictionary();
        wd.addWord("ab");
        System.out.println(wd.search("a."));
    }
}
