package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.*;

/**
 * Created by benbendaisy on 4/19/15.
 *
 * Given a binary tree, return the inorder traversal of its nodes' values.
 *
 * For example:
 * Given binary tree {1,#,2,3},
 * 1
 * \
 * 2
 * /
 * 3
 * return [1,3,2].
 * Note: Recursive solution is trivial, could you do it iteratively?
 */
public class BinaryTreeInorderTraversal {
    //iterative way with O(n) spaces
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == root) return list;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        Set<TreeNode> visited = new HashSet<TreeNode>();
        visited.add(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.peek();
            if (null != node.left && visited.add(node.left)) {
                stack.push(node.left);
            } else {
                stack.pop();
                list.add(node.val);
                if (null != node.right) {
                    stack.push(node.right);
                    visited.add(node.right);
                }
            }
        }
        return list;
    }

    //iterative way with constant space
    public List<Integer> inorderTraversalI(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == root) return list;
        TreeNode cur = root;
        while (null != cur) {
            if (null != cur.left) {
                TreeNode prev = cur.left;
                while (null != prev.right && prev.right != cur) {
                    prev = prev.right;
                }
                if (null == prev.right) {
                    prev.right = cur;
                    cur = cur.left;
                } else {
                    prev.right = null;
                    list.add(cur.val);
                    cur = cur.right;
                }
            } else {
                list.add(cur.val);
                cur = cur.right;
            }
        }
        return list;
    }

    public static void main(String[] args) {
        TreeNode node = new TreeNode(2);
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(1);
        node.left = node1;
        node1.left = node2;
        BinaryTreeInorderTraversal binaryTreeInorderTraversal = new BinaryTreeInorderTraversal();
        System.out.println(binaryTreeInorderTraversal.inorderTraversalI(node));
    }

}
