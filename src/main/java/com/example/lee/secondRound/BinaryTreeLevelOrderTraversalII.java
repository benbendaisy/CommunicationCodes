package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by benbendaisy on 4/14/15.
 *
 * Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
 *
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *  3
 *  / \
 *  9  20
 *  /  \
 *  15   7
 * return its bottom-up level order traversal as:
 * [
 * [15,7],
 * [9,20],
 * [3]
 * ]
 */
public class BinaryTreeLevelOrderTraversalII {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == root) return lli;
        Queue<TreeNode> que1 = new LinkedList<TreeNode>();
        Queue<TreeNode> que2 = new LinkedList<TreeNode>();
        que1.add(root);
        List<Integer> list = new ArrayList<Integer>();
        while (!que1.isEmpty()) {
            TreeNode node = que1.poll();
            if (null != node.left) que2.add(node.left);
            if (null != node.right) que2.add(node.right);
            list.add(node.val);
            if (que1.isEmpty()) {
                lli.add(0, list);
                list = new ArrayList<Integer>();
                que1 = que2;
                que2 = new LinkedList<TreeNode>();
            }
        }
        return lli;
    }
}
