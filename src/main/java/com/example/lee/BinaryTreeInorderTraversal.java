package com.example.lee;

import com.example.lee.model.TreeNode;

import java.util.*;

/**
 * Created by benbendaisy on 1/7/15.
 *
 * Given a binary tree, return the inorder traversal of its nodes' values.
 *
 * For example:
 * Given binary tree {1,#,2,3},
 * 1
 *  \
 *   2
 *  /
 * 3
 * return [1,3,2].
 *
 * Note: Recursive solution is trivial, could you do it iteratively?
 */
public class BinaryTreeInorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        if(root == null){
            return list;
        }
        Stack<TreeNode> stack = new Stack<TreeNode>();
        Set<TreeNode> set = new HashSet<TreeNode>();
        stack.add(root);
        while(!stack.isEmpty()){
            TreeNode node = stack.peek();
            if(set.add(node)){
                if(node.left != null){
                    stack.add(node.left);
                }
            } else {
                node = stack.pop();
                list.add(node.val);
                if(node.right != null){
                    stack.add(node.right);
                }
            }
        }
        return list;
    }

    //remove visited treenode set
    public List<Integer> inorderTraversalI(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        if(root == null){
            return list;
        }
        Stack<TreeNode> stack = new Stack<TreeNode>();

        while(true){
            while(root != null){
                stack.add(root);
                root = root.left;
            }
            if(stack.isEmpty()){
                break;
            }
            root = stack.pop();
            list.add(root.val);
            root = root.right;
        }
        return list;
    }
}
