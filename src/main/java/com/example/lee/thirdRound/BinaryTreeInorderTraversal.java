package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.*;

public class BinaryTreeInorderTraversal {
    public List<Integer> inorderTraversalI(TreeNode root) {
        if (root == null) {
            return Collections.emptyList();
        }
        List<Integer> list = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        Set<TreeNode> nodeSet = new HashSet<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.peek();
            if (nodeSet.add(node) && node.left != null) {
                stack.push(node.left);
            } else {
                node = stack.pop();
                list.add(node.val);
                if (node.right != null) {
                    stack.push(node.right);
                }
            }
        }
        return list;
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) {
            return Collections.emptyList();
        }
        List<Integer> list = new ArrayList<>();
        inorderTraversalHelper(root, list);
        return list;
    }

    private void inorderTraversalHelper(TreeNode root, List<Integer> list) {
        if (root == null) {
            return;
        }
        inorderTraversalHelper(root.left, list);
        list.add(root.val);
        inorderTraversalHelper(root.right, list);
    }

    public static void main(String[] args) {
        BinaryTreeInorderTraversal binaryTreeInorderTraversal = new BinaryTreeInorderTraversal();
        TreeNode treeNode1 = new TreeNode(1);
        TreeNode treeNode2 = new TreeNode(2);
        TreeNode treeNode3 = new TreeNode(3);
        treeNode1.right = treeNode2;
        treeNode2.left = treeNode3;
        System.out.println(binaryTreeInorderTraversal.inorderTraversalI(treeNode1));
    }
}
