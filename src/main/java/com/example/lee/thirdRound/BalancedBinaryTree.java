package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.HashMap;
import java.util.Map;

public class BalancedBinaryTree {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        Map<TreeNode, Integer> cached = new HashMap<>();
        return isBalancedHelper(root, cached);
    }

    private boolean isBalancedHelper(TreeNode root, Map<TreeNode, Integer> cached) {
        if (root == null) {
            return true;
        }
        int leftHeight = height(root.left, cached);
        int rightHeight = height(root.right, cached);
        if (Math.abs(leftHeight - rightHeight) > 1) {
            return false;
        }
        return isBalancedHelper(root.left, cached) && isBalancedHelper(root.right, cached);
    }

    private int height(TreeNode root, Map<TreeNode, Integer> cached) {
        if (cached.containsKey(root)) {
            return cached.get(root);
        }
        if (root == null) {
            return 0;
        }
        int height = 1 + Math.max(height(root.left, cached), height(root.right, cached));
        cached.put(root, height);
        return height;
    }

    public static void main(String[] args) {
        TreeNode node = new TreeNode(1);
        BalancedBinaryTree balancedBinaryTree = new BalancedBinaryTree();
        System.out.println(balancedBinaryTree.isBalanced(node));
    }
}
