package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

public class PathSum {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        return hasPathSumHelper(root, sum, 0);
    }

    private boolean hasPathSumHelper(TreeNode root, int sum, int currentSum) {
        if (root == null) {
            return sum == currentSum;
        }
        int localSum = root.val + currentSum;
        if (root.left == null && root.right == null) {
            return localSum == sum;
        } else if (root.left == null) {
            return hasPathSumHelper(root.right, sum, localSum);
        } else if (root.right == null) {
            return hasPathSumHelper(root.left, sum, localSum);
        }
        return hasPathSumHelper(root.left, sum, localSum) || hasPathSumHelper(root.right, sum, localSum);
    }
}
