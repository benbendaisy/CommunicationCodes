package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/14/15.
 */
public class BalancedBinaryTree {
    Map<TreeNode, Integer> map = new HashMap<TreeNode, Integer>();
    public boolean isBalanced(TreeNode root) {
        if (null == root) return true;
        int l = height(root.left, map);
        int r = height(root.right, map);
        if(Math.abs(l - r) > 1) return false;
        return isBalanced(root.left) && isBalanced(root.right);
    }

    private int height(TreeNode root, Map<TreeNode, Integer> map) {
        if (null == root) {
            return 0;
        } else if (map.containsKey(root)) {
            return map.get(root);
        }
        int h = 0;
        if (null == root.right) {
            h = height(root.left, map) + 1;
        } else if (null == root.left) {
            h = height(root.right, map) + 1;
        } else {
            int l = height(root.left, map) + 1;
            int r = height(root.right, map) + 1;
            h = l > r ? l : r;
        }
        map.put(root, h);
        return h;
    }
}
