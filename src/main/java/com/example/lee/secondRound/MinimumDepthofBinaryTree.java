package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 4/14/15.
 *
 * Given a binary tree, find its minimum depth.
 *
 * The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 */
public class MinimumDepthofBinaryTree {
    public int minDepth(TreeNode root) {
        if (null == root) {
            return 0;
        } else if (null == root.left && null == root.right) {
            return 1;
        } else if (null == root.right) {
            return minDepth(root.left) + 1;
        } else if (null == root.left) {
            return minDepth(root.right) + 1;
        } else {
            int left = minDepth(root.left) + 1;
            int right = minDepth(root.right) + 1;
            return left > right ? right : left;
        }
    }
}
