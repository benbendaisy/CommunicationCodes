package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

public class BinaryTreeMaximumPathSum {
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxPathSumHelper(root);
        return max;
    }

    private int maxPathSumHelper(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = maxPathSumHelper(root.left);
        int right = maxPathSumHelper(root.right);
        int localMax = root.val + Math.max(left, right);
        localMax = Math.max(localMax, root.val);
        max = Math.max(max, localMax);
        max = Math.max(max, root.val + left + right);
        return localMax;
    }
}
