package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/19/15.
 *
 * Two elements of a binary search tree (BST) are swapped by mistake.
 *
 * Recover the tree without changing its structure.
 */
public class RecoverBinarySearchTree {
    TreeNode prev = null, node1 = null, node2 = null;
    //O(1) space
    public void recoverTree(TreeNode root) {
        if (null == root) return;
        inorder(root);
        if (null != node1 && null != node2) {
            int t = node1.val;
            node1.val = node2.val;
            node2.val = t;
        }
    }

    private void inorder(TreeNode root) {
        if (null == root) return;
        inorder(root.left);
        if (null != prev && prev.val > root.val) {
            if (null == node1) {
                node1 = prev;
                node2 = root;
            } else {
                node2 = root;
                return;
            }
        }
        prev = root;
        inorder(root.right);
    }

    //O(n) space
    public void recoverTreeI(TreeNode root) {
        if (null == root) return;
        TreeNode node1 = null, node2 = null;
        List<TreeNode> lt = new ArrayList<TreeNode>();
        inorder(root, lt);
        if (lt.size() < 2) return;
        for (int i = 1; i < lt.size(); i++) {
            if (lt.get(i - 1).val > lt.get(i).val) {
                if (null == node1) {
                    node1 = lt.get(i - 1);
                    node2 = lt.get(i);
                } else {
                    node2 = lt.get(i);
                    break;
                }
            }
        }
        if (null != node1 && null != node2) {
            int t = node1.val;
            node1.val = node2.val;
            node2.val = t;
        }
    }

    private void inorder(TreeNode root, List<TreeNode> lt) {
        if (null == root) return;
        inorder(root.left, lt);
        lt.add(root);
        inorder(root.right, lt);
    }
}
