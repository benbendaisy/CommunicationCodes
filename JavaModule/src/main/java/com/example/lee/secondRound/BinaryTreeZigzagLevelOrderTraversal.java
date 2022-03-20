package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Created by benbendaisy on 4/15/15.
 *
 * Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
 *
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *   3
 *  / \
 *  9  20
 * /  \
 * 15   7
 * return its zigzag level order traversal as:
 * [
 * [3],
 * [20,9],
 * [15,7]
 * ]
 */
public class BinaryTreeZigzagLevelOrderTraversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == root) return lli;
        Stack<TreeNode> stack1 = new Stack<TreeNode>();
        Stack<TreeNode> stack2 = new Stack<TreeNode>();
        stack1.push(root);
        List<Integer> list = new ArrayList<Integer>();
        boolean leftRight = true;
        while (!stack1.isEmpty()) {
            TreeNode node = stack1.pop();
            if (leftRight) {
                if (null != node.left) stack2.push(node.left);
                if (null != node.right) stack2.push(node.right);
            } else {
                if (null != node.right) stack2.push(node.right);
                if (null != node.left) stack2.push(node.left);
            }
            list.add(node.val);
            if (stack1.isEmpty()) {
                stack1 = stack2;
                stack2 = new Stack<TreeNode>();
                lli.add(list);
                list = new ArrayList<Integer>();
                leftRight = !leftRight;
            }
        }
        return lli;
    }
}
