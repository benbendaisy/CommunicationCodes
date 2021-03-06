package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 1/3/15.
 *
 * Given preorder and inorder traversal of a tree, construct the binary tree.
 *
 * Note:
 * You may assume that duplicates do not exist in the tree.
 */
public class ConstructBinaryTreefromPreorderandInorderTraversal {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder == null || inorder == null || preorder.length != inorder.length){
            return null;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int length = inorder.length;
        for(int i = 0; i < length; i++){
            map.put(inorder[i], i);
        }
        return buildTreeHelper(preorder, inorder, 0, length - 1, 0, length -1, map);
    }

    private TreeNode buildTreeHelper(int[] preorder, int[] inorder, int start, int end, int start1, int end1, Map<Integer, Integer> map){
        if(start > end || start1 > end1 || start >= preorder.length){
            return null;
        } else if(start == end){
            return new TreeNode(preorder[start]);
        }

        TreeNode node = new TreeNode(preorder[start]);
        int leftLength = map.get(preorder[start]) - start1;
        node.left = buildTreeHelper(preorder, inorder, start + 1, start + leftLength, start1, map.get(preorder[start]) - 1, map);
        node.right = buildTreeHelper(preorder, inorder, start + leftLength + 1, end, map.get(preorder[start]) + 1, end1, map);
        return node;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] newArray = Arrays.copyOfRange(array, 1, 3);
        for(int i : newArray){
            System.out.println(i);
        }
    }
}
