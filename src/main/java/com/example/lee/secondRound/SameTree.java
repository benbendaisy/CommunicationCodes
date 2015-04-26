package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 4/18/15.
 */
public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (null == p && null == q) {
            return true;
        } else if (null == p || null == q || p.val != q.val) {
            return false;
        } else {
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
    }
}
