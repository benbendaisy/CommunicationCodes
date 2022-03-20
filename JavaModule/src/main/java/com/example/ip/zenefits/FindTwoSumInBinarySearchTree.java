package com.example.ip.zenefits;

import com.example.lee.model.TreeNode;

/**
 * Created by benben on 6/6/15.
 *
 * the problem is to find any two nodes in a binary search tree to make
 * the sum of two nodes equal to target. require O(n) time complexity and
 * O(logn) space
 *
 */
public class FindTwoSumInBinarySearchTree {
    public boolean findTwoSum (TreeNode root, int target) {
        BinarySearchTreeIterator iterator = new BinarySearchTreeIterator(root);
        if (iterator.hasSmallerNext() && iterator.hasBiggerNext()) {
            int l = iterator.nextBigger();
            int r = iterator.nextSmaller();
            while (l < r) {
                int sum = l + r;
                if (sum == target) {
                    return true;
                } else if (sum < target && iterator.hasBiggerNext()) {
                    l = iterator.nextBigger();
                } else if (sum > target && iterator.hasSmallerNext()) {
                    r = iterator.nextSmaller();
                } else {
                    return false;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        TreeNode node = new TreeNode(2);
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(3);
        TreeNode node3 = new TreeNode(4);
        TreeNode node4 = new TreeNode(6);
        node2.right = node3;
        node3.right = node4;
        node.left = node1;
        node.right = node2;
//        BinarySearchTreeIterator iterator1 = new BinarySearchTreeIterator(node);
//        BinarySearchTreeIterator iterator2 = new BinarySearchTreeIterator(node);
//        while (iterator1.hasBiggerNext()) {
//            System.out.println(iterator1.nextBigger());
//        }
//        while (iterator2.hasSmallerNext()) {
//            System.out.println(iterator2.nextSmaller());
//        }
        FindTwoSumInBinarySearchTree findTwoSumInBinarySearchTree = new FindTwoSumInBinarySearchTree();
        System.out.println(findTwoSumInBinarySearchTree.findTwoSum(node, 14));
    }
}
