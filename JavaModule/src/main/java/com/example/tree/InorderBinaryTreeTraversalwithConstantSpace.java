package com.example.tree;

import com.example.lee.model.TreeNode;

import java.util.List;

/**
 * Created by benbendaisy on 3/11/15.
 */
public class InorderBinaryTreeTraversalwithConstantSpace {
    public void inOrderMorris(TreeNode root, List<Integer> values) {
        if (null == root) {
            return;
        }

        TreeNode cur = root;
        while (null != cur) {
            if (null != cur.left) {
                TreeNode prev = cur.left;
                while (null != prev.right && prev.right != cur) {
                    prev = prev.right;
                }
                if (null == prev.right) {
                    prev.right = cur;
                    cur = cur.left;
                } else {
                    prev.right = null;
                    values.add(cur.val);
                    cur = cur.right;
                }
            } else {
                values.add(cur.val);
                cur = cur.right;
            }
        }
    }
}
