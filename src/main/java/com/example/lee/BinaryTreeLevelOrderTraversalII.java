package com.example.lee;

import com.example.lee.model.TreeNode;

import java.util.*;

/**
 * Created by benbendaisy on 1/3/15.
 *
 * Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *     3
 *    / \
 *   9  20
 *     /  \
 *    15   7
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
        Collections.reverse(lli);
        return lli;
    }
}
