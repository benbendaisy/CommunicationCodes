package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/5/15.
 *
 * Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
 *
 * For example,
 * Given n = 3, your program should return all 5 unique BST's shown below.
 *
 * 1         3     3      2      1
 *  \       /     /      / \      \
 *   3     2     1      1   3      2
 *  /     /       \                 \
 *  2     1         2                 3
 */
public class UniqueBinarySearchTreesII {
    public List<TreeNode> generateTrees(int n) {
        if(n == 0){
            List<TreeNode> lt = new ArrayList<TreeNode>();
            lt.add(null);
            return lt;
        }
        return generateTreesHelper(1, n);
    }

    public List<TreeNode> generateTreesHelper(int left, int right){
        List<TreeNode> lt = new ArrayList<TreeNode>();
        if(left > right){
            lt.add(null);
            return lt;
        }
        for(int i = left; i <= right; i++){
            List<TreeNode> leftNode = generateTreesHelper(left, i - 1);
            List<TreeNode> rightNode = generateTreesHelper(i + 1, right);
            for(TreeNode node1 : leftNode){
                for(TreeNode node2 : rightNode){
                    TreeNode node = new TreeNode(i);
                    node.left = node1;
                    node.right = node2;
                    lt.add(node);
                }
            }
        }
        return lt;
    }
}
