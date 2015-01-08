package com.example.lee;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/5/15.
 *
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 *
 * Assume a BST is defined as follows:
 *
 * The left subtree of a node contains only nodes with keys less than the node's key.
 * The right subtree of a node contains only nodes with keys greater than the node's key.
 * Both the left and right subtrees must also be binary search trees.
 */
public class ValidateBinarySearchTree {

    //pass min and max to lower level. need to handle max and min integer
    public boolean isValidBST(TreeNode root) {
        if(root == null || (root.left == null && root.right == null)){
            return true;
        }
        long min = Long.valueOf(Integer.MIN_VALUE) - 1;
        long max = Long.valueOf(Integer.MAX_VALUE) + 1;
        return isValidBST(root, min, max);
    }

    private boolean isValidBST(TreeNode root, long min, long max){
        if(root == null){
            return true;
        } else if(root.val <= min || root.val >= max){
            return false;
        } else if(root.left == null && root.right == null){
            return root.val > min && root.val < max;
        }

        return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
    }

    //translate tree to list by in order visit and check the result list to see if there
    //is any element in wrong place.
    public boolean isValidBSTI(TreeNode root) {
        if(root == null || (root.left == null && root.right == null)){
            return true;
        }

        List<Integer> li = new ArrayList<Integer>();
        treeToList(root, li);
        for(int i = 1; i < li.size(); i++){
            if(li.get(i) <= li.get(i-1)){
                return false;
            }
        }
        return true;
    }

    private void treeToList(TreeNode root, List<Integer> li){
        if(root == null){
            return;
        }
        treeToList(root.left, li);
        li.add(root.val);
        treeToList(root.right, li);
    }

    public static void main(String[] args) {
        TreeNode node1 = new TreeNode(0);
        TreeNode node2 = new TreeNode(-1);
        node1.left = node2;
        ValidateBinarySearchTree validateBinarySearchTree = new ValidateBinarySearchTree();
        System.out.println(validateBinarySearchTree.isValidBST(node1));
    }
}
