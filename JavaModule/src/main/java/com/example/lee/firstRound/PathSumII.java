package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/3/15.
 * Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
 *
 * For example:
 * Given the below binary tree and sum = 22,
 *      5
 *     / \
 *    4   8
 *    /   / \
 *   11  13  4
 *  /  \      \
 * 7    2      1
 * return
 * [
 * [5,4,11,2],
 * [5,8,4,5]
 * ]
 */
public class PathSumII {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if(root == null){
            return lli;
        }
        List<Integer> li = new ArrayList<Integer>();
        pathSumHelper(root, sum, li, lli);
        return lli;
    }

    private void pathSumHelper(TreeNode root, int sum, List<Integer> li, List<List<Integer>> lli){
        if(root == null){
            return;
        }

        List<Integer> newLi = new ArrayList<Integer>(li);
        newLi.add(root.val);
        if(root.left == null && root.right == null && root.val == sum){
            lli.add(newLi);
            return;
        }
        int currentSum = sum - root.val;
        pathSumHelper(root.left, currentSum, newLi, lli);
        pathSumHelper(root.right, currentSum, newLi, lli);
    }
}
