package com.example.ip;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

/**
 * Created by benbendaisy on 5/1/15.
 */
public class WorldGame {
    static private class TreeNode {
        char ch;
        int cnt;
        List<TreeNode> childList;
        public TreeNode(char ch) {
            childList = new LinkedList<TreeNode>();
            this.ch = ch;
            cnt = 0;
        }
        public TreeNode getChildNode(char ch) {
            if (childList != null) {
                for (TreeNode node : childList) {
                    if (ch == node.ch) return node;
                }
            }
            return null;
        }
    }

    static class Tree {
        private TreeNode root;
        public Tree() {
            root = new TreeNode(' ');
        }
        public void insert(String word) {
            TreeNode cur = root;
            int level = 0;
            for (char ch : word.toCharArray()) {
                TreeNode child = cur.getChildNode(ch);
                if (child != null) {
                    cur = child;
                } else {
                    cur.childList.add(new TreeNode(ch));
                    cur = cur.getChildNode(ch);
                }
                cur.cnt++;
            }
        }

        public int getPathCount(String word) {
            if (word == null || word.length() < 1) return 0;
            TreeNode cur = root;
            int cnt = 0;
            int level = 0;
            for (char ch : word.toCharArray()) {
                TreeNode child = cur.getChildNode(ch);
                level++;
                if (child != null) {
                    cur = child;
                    cnt += cur.cnt * level;
                } else {
                    break;
                }
            }
            return cnt;
        }

        public boolean search(String word) {
            if (word == null || word.length() < 1) return false;
            TreeNode cur = root;
            for (char ch : word.toCharArray()) {
                TreeNode child = cur.getChildNode(ch);
                if (child != null) {
                    cur = child;
                } else {
                    return false;
                }
            }
            return true;
        }

        public void remove(String word) {
            if (null == word || word.length() < 1) return;
            if (!search(word)) return;
            TreeNode cur = root;
            for (char ch : word.toCharArray()) {
                TreeNode child = cur.getChildNode(ch);
                if (child != null) {
                    if (child != null) {
                        child.cnt--;
                        if (child.cnt < 0) child.cnt = 0;
                        cur = child;
                    } else {
                        return;
                    }
                } else {
                    return;
                }
            }
        }
    }
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner scan = new Scanner(System.in);
        Tree root = new Tree();
        int cnt = 0;
        int n = Integer.parseInt(scan.nextLine());
        while (n > 0) {
            String word = scan.nextLine();
            if (null != word) {
                word = word.trim();
                if (word.length() > 2) {
                    String newWord = word.substring(2);
                    if (word.startsWith("+")) {
                        cnt = root.getPathCount(newWord);
                        System.out.println(cnt);
                        root.insert(newWord);
                    } else if (word.startsWith("-")) {
                        root.remove(newWord);
                    }
                }
            }
            n--;
        }
    }
}
