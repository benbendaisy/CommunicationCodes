package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

public class FlattenBinaryTreeToLinkedList {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }

        TreeNode cur = root;
        while (cur != null) {
            if (cur.left != null) {
                TreeNode rightMostNode = findRightMostNode(cur.left);
                rightMostNode.right = cur.right;
                cur.right = cur.left;
                cur.left = null;
            }
            cur = cur.right;
        }
    }

    private TreeNode findRightMostNode(TreeNode root) {
        while (root != null && root.right != null) {
            root = root.right;
        }
        return root;
    }
}
