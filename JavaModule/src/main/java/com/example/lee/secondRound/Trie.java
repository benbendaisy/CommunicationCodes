package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/8/15.
 */

class TrieNode {
    // Initialize your data structure here.
    char ch;
    boolean isEnd;
    List<TrieNode> children;
    public TrieNode() {
        children = new ArrayList<TrieNode>();
    }

    public TrieNode getChild(char ch) {
        if (null != children) {
            for (TrieNode node : children) {
                if (node.ch == ch) {
                    return node;
                }
            }
        }
        return null;
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        if (null == word || word.length() < 1 || search(word)) return;
        TrieNode node = root.getChild(word.charAt(0));
        if (null == node) {
            node = new TrieNode();
            node.ch = word.charAt(0);
            root.children.add(node);
        }
        for (int i = 1; i < word.length(); i++) {
            char ch = word.charAt(i);
            TrieNode newNode = node.getChild(ch);
            if (newNode == null) {
                newNode = new TrieNode();
                newNode.ch = ch;
                node.children.add(newNode);
            }
            node = newNode;
        }
        node.isEnd = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        if (null == word || word.length() < 1) return false;
        TrieNode node = root.getChild(word.charAt(0));
        if (null == node) return false;
        for (int i = 1; i < word.length(); i++) {
            char ch = word.charAt(i);
            TrieNode newNode = node.getChild(ch);
            if (null == newNode) {
                return false;
            }
            node = newNode;
        }
        return node.isEnd;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        if (null == prefix || prefix.length() < 1) return false;
        TrieNode node = root.getChild(prefix.charAt(0));
        if (null == node) return false;
        for (int i = 1; i < prefix.length(); i++) {
            char ch = prefix.charAt(i);
            TrieNode newNode = node.getChild(ch);
            if (newNode == null) {
                return false;
            }
            node = newNode;
        }
        return true;
    }
}