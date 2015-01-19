package com.example.lee;

import com.example.lee.model.TreeNode;

import java.util.Stack;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
 *
 * Calling next() will return the next smallest number in the BST.
 *
 * Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
 */
public class BinarySearchTreeIterator {
    Stack<TreeNode> stack = new Stack<TreeNode>();
    public BinarySearchTreeIterator(TreeNode root) {
        while(root != null){
            stack.push(root);
            root = root.left;
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        if(!stack.isEmpty()){
            TreeNode root = stack.pop();
            TreeNode right = root.right;
            while(right != null){
                stack.push(right);
                right = right.left;
            }
            return root.val;
        }
        return 0;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
