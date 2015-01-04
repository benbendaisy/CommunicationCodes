package com.example.lee;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 1/3/15.
 *
 * Given a binary tree, flatten it to a linked list in-place.
 * For example,
 * Given
 *
 *    1
 *   / \
 *  2   5
 *  / \   \
 * 3   4   6
 * The flattened tree should look like:
 *  1
 *   \
 *    2
 *     \
 *      3
 *       \
 *        4
 *         \
 *          5
 *           \
 *            6
 */
public class FlattenBinaryTreetoLinkedList {

    //recursive solution
    public void flatten(TreeNode root) {
        if(root == null){
            return;
        }
        if(root.left != null){
            TreeNode node = findRightMostNode(root.left);
            node.right = root.right;
            root.right = root.left;
            root.left = null;
        }
        flatten(root.right);
    }

    private TreeNode findRightMostNode(TreeNode root){
        while(root != null && root.right != null){
            root = root.right;
        }

        return root;
    }

    //non recursive solution
    public void flattenI(TreeNode root) {
        if(root == null){
            return;
        }
        while(root != null){
            if(root.left != null){
                TreeNode node = findRightMostNode(root.left);
                node.right = root.right;
                root.right = root.left;
                root.left = null;
            }
            root = root.right;
        }
    }
}
