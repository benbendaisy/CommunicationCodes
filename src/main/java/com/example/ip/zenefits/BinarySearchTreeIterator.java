package com.example.ip.zenefits;

import com.example.lee.model.TreeNode;

import java.util.Stack;

/**
 * Created by benbendaisy on 6/6/15.
 */
public class BinarySearchTreeIterator {
    Stack<TreeNode> minStack = new Stack<>();
    Stack<TreeNode> maxStack = new Stack<>();
    public BinarySearchTreeIterator(TreeNode node) {
        TreeNode t = node;
        while (null != t) {
            minStack.push(t);
            t = t.left;
        }
        t = node;
        while (null != t) {
            maxStack.push(t);
            t = t.right;
        }
    }

    public boolean hasBiggerNext() {
        return !minStack.isEmpty();
    }

    public boolean hasSmallerNext() {
        return !maxStack.isEmpty();
    }

    public int nextBigger() {
        if (!minStack.isEmpty()) {
            TreeNode node = minStack.pop();
            TreeNode right = node.right;
            while (null != right) {
                minStack.push(right);
                right = right.left;
            }
            return node.val;
        }
        return -1;
    }

    public int nextSmaller() {
        if (!maxStack.isEmpty()) {
            TreeNode node = maxStack.pop();
            TreeNode left = node.left;
            while (null != left) {
                maxStack.push(left);
                left = left.right;
            }
            return node.val;
        }
        return -1;
    }
}
