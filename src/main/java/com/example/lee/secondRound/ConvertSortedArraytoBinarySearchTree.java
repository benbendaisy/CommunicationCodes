package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 4/14/15.
 */
public class ConvertSortedArraytoBinarySearchTree {
    public TreeNode sortedArrayToBST(int[] num) {
        if (null == num) return null;
        return sortedArrayToBST(num, 0, num.length - 1);
    }

    public TreeNode sortedArrayToBST(int[] num, int l, int r) {
        if (l > r) return null;
        int mid = (l + r) / 2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = sortedArrayToBST(num, l, mid - 1);
        node.right = sortedArrayToBST(num, mid + 1, r);
        return node;
    }
}
