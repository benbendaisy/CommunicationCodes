package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/15/15.
 *
 * Given inorder and postorder traversal of a tree, construct the binary tree.
 *
 * Note:
 * You may assume that duplicates do not exist in the tree.
 */
public class ConstructBinaryTreefromInorderandPostorderTraversal {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (null == inorder || null == postorder || inorder.length != postorder.length) return null;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }
        return buildTree(postorder, map, 0, postorder.length - 1, 0);
    }

    public TreeNode buildTree(int[] postorder, Map<Integer, Integer> map, int pl, int pr, int s) {
        if (pl > pr) {
            return null;
        } else if (pl == pr) {
            return new TreeNode(postorder[pr]);
        }
        TreeNode node = new TreeNode(postorder[pr]);
        int len = map.get(postorder[pr]) - s;
        if (len < 0) return node;
        node.left = buildTree(postorder, map, pl, pl + len - 1, s);
        node.right = buildTree(postorder, map, pl + len, pr - 1, map.get(postorder[pr]) + 1);
        return node;
    }
}
