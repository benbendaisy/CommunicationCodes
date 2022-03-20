package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Created by benbendaisy on 1/4/15.
 * Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
 *
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *        3
 *       / \
 *      9  20
 *     /  \
 *    15   7
 * return its level order traversal as:
 * [
 * [3],
 * [20,9],
 * [15,7]
 * ]
 */
public class BinaryTreeZigzagLevelOrderTraversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if(root == null){
            return lli;
        }

        Stack<TreeNode> stack = new Stack<TreeNode>();
        Stack<TreeNode> stack1 = new Stack<TreeNode>();
        stack.push(root);
        List<Integer> li = new ArrayList<Integer>();
        boolean leftToRight = true;
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            li.add(node.val);
            if(leftToRight){
                if(node.left != null){
                    stack1.push(node.left);
                }
                if(node.right != null){
                    stack1.push(node.right);
                }
            } else {
                if(node.right != null){
                    stack1.push(node.right);
                }
                if(node.left != null){
                    stack1.push(node.left);
                }
            }

            if(stack.isEmpty()){
                stack = stack1;
                stack1 = new Stack<TreeNode>();
                lli.add(li);
                li = new ArrayList<Integer>();
                leftToRight = !leftToRight;
            }
        }
        return lli;
    }
}
