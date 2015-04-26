package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/19/15.
 *
 * Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
 *
 * For example,
 * Given n = 3, your program should return all 5 unique BST's shown below.
 *
 * 1         3     3      2      1
 * \       /     /      / \      \
 * 3     2     1      1   3      2
 * /     /       \                 \
 * 2     1         2                 3
 */
public class UniqueBinarySearchTreesII {
    public List<TreeNode> generateTrees(int n) {
        if (n < 1) {
            List<TreeNode> list = new ArrayList<TreeNode>();
            list.add(null);
            return list;
        }
        return generateTrees(1, n);
    }
    private List<TreeNode> generateTrees(int left, int right) {
        List<TreeNode> lt = new ArrayList<TreeNode>();
        if (left > right) {
            lt.add(null);
            return lt;
        }
        for (int i = left; i <= right; i++) {
            List<TreeNode> leftTree = generateTrees(left, i - 1);
            List<TreeNode> rightTree = generateTrees(i + 1, right);
            for (TreeNode node1 : leftTree) {
                for (TreeNode node2 : rightTree) {
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
