package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/15/15.
 *
 * Given preorder and inorder traversal of a tree, construct the binary tree.
 *
 * Note:
 * You may assume that duplicates do not exist in the tree.
 */
public class ConstructBinaryTreefromPreorderandInorderTraversal {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (null == preorder || null == inorder || preorder.length != inorder.length || preorder.length == 0) return null;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }
        return buildTree(preorder, map, 0, preorder.length - 1, 0);
    }

    private TreeNode buildTree(int[] preorder, Map<Integer, Integer> map, int pl, int pr, int il) {
        if (pl > pr || pl >= preorder.length) return null;
        if (pl == pr) return new TreeNode(preorder[pl]);
        TreeNode node = new TreeNode(preorder[pl]);
        int length = map.get(preorder[pl]) - il;
        if (length < 0) return node;
        node.left = buildTree(preorder, map, pl + 1, pl + length, il);
        node.right = buildTree(preorder, map, pl + length + 1, pr, map.get(preorder[pl]) + 1);
        return node;
    }
}
