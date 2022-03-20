package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 6/8/15.
 *
 *
 */
public class CountCompleteTreeNodes {
    public int countNodes(TreeNode root) {
        if (null == root) return 0;
        int l = getLeft(root.left) + 1;
        int r = getRight(root.right) + 1;
        if (l == r) {
            return (2 << (l - 1)) - 1;
        } else {
            return 1 + countNodes(root.left) + countNodes(root.right);
        }
    }

    private int getLeft(TreeNode root) {
        if (null == root) return 0;
        int h = 0;
        while (null != root) {
            h++;
            root = root.left;
        }
        return h;
    }

    private int getRight(TreeNode root) {
        if (null == root) return 0;
        int h = 0;
        while (null != root) {
            h++;
            root = root.right;
        }
        return h;
    }

    public int countNodesI(TreeNode root) {
        if (null == root) return 0;
        return 1 + countNodesI(root.left) + countNodesI(root.right);
    }
}
