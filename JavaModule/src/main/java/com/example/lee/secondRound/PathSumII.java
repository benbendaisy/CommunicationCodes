package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/14/15.
 *
 * Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
 *
 * For example:
 * Given the below binary tree and sum = 22,
 *   5
 *  / \
 * 4   8
 * /   / \
 * 11  13  4
 * /  \    / \
 * 7    2  5   1
 * return
 * [
 * [5,4,11,2],
 * [5,8,4,5]
 * ]
 */
public class PathSumII {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (null == root) return lli;
        List<Integer> li = new ArrayList<Integer>();
        pathSum(root, sum, lli, li);
        return lli;
    }

    public void pathSum(TreeNode root, int sum, List<List<Integer>> lli, List<Integer> li) {
        if (null == root) {
            return;
        } else if (null == root.left && null == root.right) {
            if (sum == root.val) {
                li.add(root.val);
                lli.add(li);
            }
            return;
        } else {
            List<Integer> newLeft = new ArrayList<Integer>(li);
            newLeft.add(root.val);
            int l = sum - root.val;
            pathSum(root.left, l, lli, newLeft);
            List<Integer> newRight = new ArrayList<Integer>(li);
            newRight.add(root.val);
            pathSum(root.right, l, lli, newRight);
        }
    }
}
