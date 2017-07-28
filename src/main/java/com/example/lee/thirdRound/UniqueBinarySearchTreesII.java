package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;
import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class UniqueBinarySearchTreesII {
    public List<TreeNode> generateTrees(int n) {
        if (n < 1) {
            return Collections.emptyList();
        }
        return generateTreesHelper(1, n);
    }

    private List<TreeNode> generateTreesHelper(int left, int right) {
        if (left > right) {
            List<TreeNode> list = new ArrayList<>();
            list.add(null);
            return list;
        }
        List<TreeNode> list = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            List<TreeNode> leftNodes = generateTreesHelper(left, i - 1);
            List<TreeNode> rightNodes = generateTreesHelper(i + 1, right);
            for (TreeNode leftNode : leftNodes) {
                for (TreeNode rightNode : rightNodes) {
                    TreeNode node = new TreeNode(i);
                    node.left = leftNode;
                    node.right = rightNode;
                    list.add(node);
                }
            }
        }
        return list;
    }

    public static void main(String[] args) {
        UniqueBinarySearchTreesII uniqueBinarySearchTreesII = new UniqueBinarySearchTreesII();
        List<TreeNode> list = Arrays.asList(null);
        System.out.println(list.get(0));
    }
}
