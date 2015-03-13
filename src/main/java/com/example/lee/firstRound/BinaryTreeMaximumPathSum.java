package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 12/30/14.
 *
 * Given a binary tree, find the maximum path sum.
 * The path may start and end at any node in the tree.
 * For example:
 * Given the below binary tree,
 *   1
 *  / \
 * 2   3
 * Return 6.
 */
public class BinaryTreeMaximumPathSum {
    private int max = -10000;
    public int maxPathSum(TreeNode root) {
        if(root == null){
            return 0;
        }
        Map<TreeNode, Integer> map = new HashMap<TreeNode, Integer>();
        maxPathSumHelper(root, map);
        return max;
    }

    private int maxPathSumHelper(TreeNode root, Map<TreeNode, Integer> map){

        if(root == null){
            return -1000;
        } else if(map.containsKey(root)){
            return map.get(root);
        }

        int leftMax = maxPathSumHelper(root.left, map);
        int rightMax = maxPathSumHelper(root.right, map);

        //local max can be left path, right path or the node itself
        int localMax = Math.max(leftMax + root.val, rightMax + root.val);
        localMax = Math.max(localMax, root.val);

        //max can be the path that includes left path, the node and the right path
        max = Math.max(max, Math.max(localMax, leftMax + rightMax + root.val));

        map.put(root, localMax);
        return localMax;

    }

    public static void main(String[] args) {
        BinaryTreeMaximumPathSum tree = new BinaryTreeMaximumPathSum();
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        node1.left = node2;
        node1.right = node3;
        System.out.println(tree.maxPathSum(node1));
    }
}
