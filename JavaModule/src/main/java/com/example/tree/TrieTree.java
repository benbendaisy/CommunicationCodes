package com.example.tree;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by pzhong1 on 5/1/15.
 */
public class TrieTree {
    private class TrieNode {
        char ch;
        boolean isEnd;
        int count;
        List<TrieNode> childTrieNodes;

        public TrieNode(char c) {
            childTrieNodes = new LinkedList<TrieNode>();
            isEnd = false;
            ch = c;
            count = 0;
        }

        public TrieNode getChildNode(char c) {
            if (childTrieNodes != null)
                for (TrieNode node : childTrieNodes)
                    if (node.ch == c)
                        return node;
            return null;
        }
    }

    private TrieNode root;

    public TrieTree() {
        root = new TrieNode(' ');
    }

    public void insert(String word) {
        if (search(word) == true)
            return;
        TrieNode current = root;
        for (char ch : word.toCharArray()) {
            TrieNode child = current.getChildNode(ch);
            if (child != null)
                current = child;
            else {
                current.childTrieNodes.add(new TrieNode(ch));
                current = current.getChildNode(ch);
            }
            current.count++;
        }
        current.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode cur = root;
        for (char ch : word.toCharArray()) {
            if (cur.getChildNode(ch) == null)
                return false;
            else
                cur = cur.getChildNode(ch);
        }
        if (cur.isEnd) return true;
        return false;
    }

    public void remove(String word) {
        if (search(word) == false) {
            System.out.println(String.format("word %s", " does not exist in this trie"));
            return;
        }
        TrieNode cur = root;
        for (char ch : word.toCharArray()) {
            TrieNode child = cur.getChildNode(ch);
            if (child.count == 1) {
                cur.childTrieNodes.remove(child);
                return;
            } else {
                child.count--;
                cur = child;
            }
        }
        cur.isEnd = false;
    }
}
