package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 3/16/15.
 *
 * Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
 * For example:
 * Given a binary tree {1,2,3,4,5},
 *     1
 *    / \
 *   2   3
 *  / \
 * 4   5
 * return the root of the binary tree [4,5,2,#,#,3,1].
 *      4
 *     / \
 *    5   2
 *       / \
 *      3   1
 */
public class BinaryTreeUpsideDown {

    //refer to http://www.cnblogs.com/EdwardLiu/p/4232896.html
    private TreeNode head = null;
    public TreeNode UpsideDownBinaryTree(TreeNode root) {
        if (null == root) {
            return null;
        }
        return head;
    }

    private TreeNode treeHelper(TreeNode root) {
        if (null == root.left) {
            head = root;
            return root;
        }
        TreeNode newRoot = treeHelper(root.left);
        newRoot.left = root.right;
        newRoot.right = root;
        return newRoot.right;
    }
}
