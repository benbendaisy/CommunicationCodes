package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

public class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        return isValidBSTHelper(root, (long) Integer.MIN_VALUE - 1, (long) Integer.MAX_VALUE + 1);
    }

    private boolean isValidBSTHelper(TreeNode root, long left, long right) {
        if (root == null) {
            return true;
        }
        return left < root.val && right > root.val
                && isValidBSTHelper(root.left, left, root.val)
                && isValidBSTHelper(root.right, root.val, right);
    }

    public static void main(String[] args) {
        ValidateBinarySearchTree validateBinarySearchTree = new ValidateBinarySearchTree();
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        node2.left = node1;
        node2.right = node3;
        System.out.println(validateBinarySearchTree.isValidBST(node2));
    }

}
