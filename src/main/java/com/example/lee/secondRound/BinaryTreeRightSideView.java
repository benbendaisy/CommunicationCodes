package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.*;

/**
 * Created by benbendaisy on 4/8/15.
 * Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
 *
 * For example:
 * Given the following binary tree,
 *     1            <---
 *   /   \
 *   2    3         <---
 *   \     \
 *    5     4       <---
 * You should return [1, 3, 4].
 */
public class BinaryTreeRightSideView {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == root) return list;
        Queue<TreeNode> que1 = new LinkedList<TreeNode>();
        Queue<TreeNode> que2 = new LinkedList<TreeNode>();
        que1.add(root);
        while (!que1.isEmpty()) {
            TreeNode node = que1.poll();
            if (null != node.left) {
                que2.add(node.left);
            }
            if (null != node.right) {
                que2.add(node.right);
            }
            if (que1.isEmpty()) {
                list.add(node.val);
                que1 = que2;
                que2 = new LinkedList<TreeNode>();
            }
        }
        return list;
    }
}
