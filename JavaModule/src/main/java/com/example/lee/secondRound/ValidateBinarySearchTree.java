package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/19/15.
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 *
 * Assume a BST is defined as follows:
 *
 * The left subtree of a node contains only nodes with keys less than the node's key.
 * The right subtree of a node contains only nodes with keys greater than the node's key.
 * Both the left and right subtrees must also be binary search trees.
 */
public class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        if (null == root || (null == root.left && null == root.right)) return true;
        return isValidBST(root, Long.valueOf(Integer.MIN_VALUE) - 1, Long.valueOf(Integer.MAX_VALUE) + 1);
    }

    private boolean isValidBST(TreeNode root, long min, long max) {
        if (null == root) {
            return true;
        } else if (root.val <= min || root.val >= max) {
            return false;
        } else if (null == root.left && null == root.right) {
            return root.val > min && root.val < max;
        }
        return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
    }

    public boolean isValidBSTI(TreeNode root) {
        if (null == root || (null == root.left && null == root.right)) return true;
        List<Integer> li = new ArrayList<Integer>();
        inOrder(root, li);
        for (int i = 1; i < li.size(); i++) {
            if (li.get(i - 1) >= li.get(i)) return false;
        }
        return true;
    }

    private void inOrder(TreeNode root, List<Integer> li) {
        if (null == root) return;
        inOrder(root.left, li);
        li.add(root.val);
        inOrder(root.right, li);
    }
}
