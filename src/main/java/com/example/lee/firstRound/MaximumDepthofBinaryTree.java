package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 1/4/15.
 *
 * Given a binary tree, find its maximum depth.
 * The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 */
public class MaximumDepthofBinaryTree {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        } else if(root.left == null && root.right == null){
            return 1;
        } else if(root.left == null){
            return maxDepth(root.right) + 1;
        } else if(root.right == null){
            return maxDepth(root.left) + 1;
        } else {
            return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
        }
    }

}
