package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Created by pzhong1 on 12/16/14.
 * Given a binary tree, return the postorder traversal of its nodes' values.
 * For example:
 * Given binary tree {1,#,2,3},
 *  1
 *   \
 *    2
 *   /
 *  3
 * return [3,2,1].
 * Note: Recursive solution is trivial, could you do it iteratively?
 */
public class BinaryTreePostorderTraversal {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> lTree = new ArrayList<Integer>();
        if(root == null){
            return lTree;
        }
        Stack<TreeNode> st = new Stack<TreeNode>();
        st.push(root);
        while(!st.isEmpty()){
            TreeNode current = st.pop();
            if(current.right != null){
                TreeNode right = current.right;
                TreeNode left = current.left;
                current.right = null;
                st.push(current);
                st.push(right);
                if(left != null){
                    st.push(left);
                    current.left = null;
                }
            } else if(current.left != null){
                TreeNode left = current.left;
                current.left = null;
                st.push(current);
                st.push(left);
            } else {
                lTree.add(current.val);
            }
        }
        //postorderTraversalHelper(root, lTree);
        return lTree;
    }
    private void postorderTraversalHelper(TreeNode root, List<Integer> lTree){
        if(root == null){
            return;
        }
        postorderTraversalHelper(root.left, lTree);
        postorderTraversalHelper(root.right, lTree);
        lTree.add(root.val);
    }
}
