package com.example.lee;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by benbendaisy on 1/4/15.
 *
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
 * [9,20],
 * [15,7]
 * ]
 */
public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if(root == null){
            return lli;
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        Queue<TreeNode> queue1 = new LinkedList<TreeNode>();
        queue.add(root);
        List<Integer> li = new ArrayList<Integer>();
        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            li.add(node.val);
            if(node.left != null){
                queue1.add(node.left);
            }
            if(node.right != null){
                queue1.add(node.right);
            }
            if(queue.isEmpty()){
                queue = queue1;
                queue1 = new LinkedList<TreeNode>();
                lli.add(li);
                li = new ArrayList<Integer>();
            }
        }
        return lli;
    }
}
