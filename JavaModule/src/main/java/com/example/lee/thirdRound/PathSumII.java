package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PathSumII {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if (root == null) {
            return Collections.emptyList();
        }
        List<List<Integer>> lists = new ArrayList<>();
        pathSumHelper(root, sum, 0, new ArrayList<>(), lists);
        return lists;
    }

    private void pathSumHelper(TreeNode root, int sum, int currentSum,
                               List<Integer> list, List<List<Integer>> lists) {
        currentSum += root.val;
        if (root.left == null && root.right == null) {
            if (currentSum == sum) {
                list.add(root.val);
                lists.add(list);
            }
            return;
        }
        if (root.left != null) {
            List<Integer> newList = new ArrayList<>(list);
            newList.add(root.val);
            pathSumHelper(root.left, sum, currentSum, newList, lists);
        }
        if (root.right != null) {
            List<Integer> newList = new ArrayList<>(list);
            newList.add(root.val);
            pathSumHelper(root.right, sum, currentSum, newList, lists);
        }
    }
}
