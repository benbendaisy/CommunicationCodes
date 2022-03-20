package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

public class MinimumDepthOfBinaryTree {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return minDepthHelper(root);
    }

    private int minDepthHelper(TreeNode root) {
        if (root.left == null && root.right == null) {
            return 1;
        } else if (root.left == null) {
            return 1 + minDepthHelper(root.right);
        } else if (root.right == null) {
            return 1 + minDepthHelper(root.left);
        }
        return 1 + Math.min(minDepthHelper(root.left), minDepthHelper(root.right));
    }

    public static void main(String[] args) {
        MinimumDepthOfBinaryTree minimumDepthOfBinaryTree = new MinimumDepthOfBinaryTree();
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        node1.left = node2;
        System.out.println(minimumDepthOfBinaryTree.minDepth(node1));
    }
}
