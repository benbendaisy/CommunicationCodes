package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 1/3/15.
 * Given a binary tree, determine if it is height-balanced.
 *
 * For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
 */
public class BalancedBinaryTree {
    Map<TreeNode, Integer> map = new HashMap<TreeNode, Integer>();
    public boolean isBalanced(TreeNode root) {
        if(root == null){
            return true;
        }
        int leftHeight = getHeight(root.left, map);
        int rightHeight = getHeight(root.right, map);
        if(Math.abs(leftHeight - rightHeight) > 1) {
            return false;
        } else {
            return isBalanced(root.left) && isBalanced(root.right);
        }
    }

    private int getHeight(TreeNode root, Map<TreeNode, Integer> map){
        if(root == null){
            return 0;
        } else if(map.containsKey(root)){
            return map.get(root);
        }
        int height = 0;
        if(root.left == null){
            height = getHeight(root.right, map) + 1;
        } else if(root.right == null){
            height = getHeight(root.left, map) + 1;
        } else {
            height = Math.max(getHeight(root.left, map) + 1, getHeight(root.right, map) + 1);
        }

        map.put(root, height);
        return height;
    }
}
