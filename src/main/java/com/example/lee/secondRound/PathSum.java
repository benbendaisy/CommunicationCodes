package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 4/14/15.
 *
 * Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
 *
 * For example:
 * Given the below binary tree and sum = 22,
 *    5
 *   / \
 *  4   8
 * /   / \
 * 11  13  4
 * /  \      \
 * 7    2      1
 * return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
 */
public class PathSum {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (null == root) {
            return false;
        } else if (null == root.left && null == root.right) {
            if (sum == root.val) {
                return true;
            } else {
                return false;
            }
        } else {
            int left = sum - root.val;
            return hasPathSum(root.left, left) || hasPathSum(root.right, left);
        }
    }
}
