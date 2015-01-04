package com.example.lee;

import com.example.lee.model.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 1/3/15.
 * Given inorder and postorder traversal of a tree, construct the binary tree.
 *
 * Note:
 * You may assume that duplicates do not exist in the tree.
 */
public class ConstructBinaryTreefromInorderandPostorderTraversal {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(inorder == null || postorder == null || inorder.length != postorder.length){
            return null;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < postorder.length; i++){
            map.put(inorder[i], i);
        }
        int length = inorder.length;
        return buildTreeHelper(inorder, postorder, 0, length - 1, 0, length -1, map);
    }

    private TreeNode buildTreeHelper(int[] inorder, int[] postorder, int start, int end, int start1, int end1, Map<Integer, Integer> map){
        if(start > end || start1 > end1){
            return null;
        }
        TreeNode node = new TreeNode(postorder[end1]);
        if(map.containsKey(postorder[end1])){
            int end2 =  map.get(postorder[end1]) - 1;
            int end3 = start1 + end2 - start;
            node.left = buildTreeHelper(inorder, postorder, start, end2, start1, end3, map);
            node.right = buildTreeHelper(inorder, postorder, end2 + 2, end, end3 + 1, end1 - 1, map);
        }

        return node;
    }
}
