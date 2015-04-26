package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 4/14/15.
 * <p/>
 * Given a binary tree, flatten it to a linked list in-place.
 * <p/>
 * For example,
 * Given
 * <p/>
 * 1
 * / \
 * 2   5
 * / \   \
 * 3   4   6
 * The flattened tree should look like:
 * 1
 * \
 * 2
 * \
 * 3
 * \
 * 4
 * \
 * 5
 * \
 * 6
 */
public class FlattenBinaryTreetoLinkedList {
    public void flatten(TreeNode root) {
        if (null == root) return;
        while (null != root) {
            TreeNode right = root.right;
            if (null != root.left) {
                root.right = root.left;
                findRightMost(root.left).right = right;
                root.left = null;
            }
            root = root.right;
        }
    }

    private TreeNode findRightMost(TreeNode root) {
        while (null != root && null != root.right) {
            root = root.right;
        }
        return root;
    }
}
