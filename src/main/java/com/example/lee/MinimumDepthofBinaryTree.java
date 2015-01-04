package com.example.lee;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 1/3/15.
 * Given a binary tree, find its minimum depth.
 * The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 */
public class MinimumDepthofBinaryTree {
    public int minDepth(TreeNode root) {
        if(root == null){
            return 0;
        } else if(root.left == null && root.right == null){
            return 1;
        }
        if(root.left == null){
            return minDepth(root.right) + 1;
        } else if(root.right == null){
            return minDepth(root.left) + 1;
        } else {
            return Math.min(minDepth(root.left) + 1, minDepth(root.right) + 1);
        }
    }
}
