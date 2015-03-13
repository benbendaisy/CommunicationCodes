package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Created by pzhong1 on 12/16/14.
 * Given a binary tree, return the preorder traversal of its nodes' values.

 * For example:
 * Given binary tree {1,#,2,3},
 *   1
 *    \
 *     2
 *    /
 *  3
 * return [1,2,3].

 * Note: Recursive solution is trivial, could you do it iteratively?
 */
public class BinaryTreePreorderTraversal {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> lTree = new ArrayList<Integer>();
        if(root == null){
            return lTree;
        }
        Stack<TreeNode> st = new Stack<TreeNode>();
        st.push(root);
        while(!st.isEmpty()){
            TreeNode current = st.pop();
            lTree.add(current.val);
            if(current.right != null){
                st.push(current.right);
            }
            if(current.left != null){
                st.push(current.left);
            }
        }
        //preorderTraversalHelper(root, lTree);
        return lTree;
    }

    private void preorderTraversalHelper(TreeNode root, List<Integer> lTree){
        if(root == null){
            return;
        }
        lTree.add(root.val);
        preorderTraversalHelper(root.left, lTree);
        preorderTraversalHelper(root.right, lTree);
    }
}
