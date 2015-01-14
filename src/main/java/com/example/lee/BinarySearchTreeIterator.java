package com.example.lee;

import com.example.lee.model.TreeNode;

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
    public BinarySearchTreeIterator(TreeNode root) {

    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return true;
    }

    /** @return the next smallest number */
    public int next() {
        return 0;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
