package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 1/3/15.
 *
 *
 */
public class ConvertSortedArraytoBinarySearchTree {
    public TreeNode sortedArrayToBST(int[] num) {
        if(num == null || num.length == 0){
            return null;
        }
        return sortedArrayToBST(num, 0, num.length - 1);
    }

    public TreeNode sortedArrayToBST(int[] num, int start, int end) {
        if(start > end){
            return null;
        }

        int mid = (start + end) / 2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = sortedArrayToBST(num, start, mid - 1);
        node.right = sortedArrayToBST(num, mid + 1, end);

        return node;
    }
}
