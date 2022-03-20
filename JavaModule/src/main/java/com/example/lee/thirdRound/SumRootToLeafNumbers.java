package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class SumRootToLeafNumbers {
    public int sumNumbers(TreeNode root) {
        if (root == null) {
            return 0;
        }
        List<String> candidates = new ArrayList<>();
        getAllPaths(root, "", candidates);
        return candidates.stream().mapToInt(x -> Integer.parseInt(x)).sum();
    }

    private void getAllPaths(TreeNode root, String str, List<String> candidates) {
        String newStr = str + root.val;
        if (root.left == null && root.right == null) {
            candidates.add(newStr);
            return;
        }
        if (root.left != null) {
            getAllPaths(root.left, newStr, candidates);
        }
        if (root.right != null) {
            getAllPaths(root.right, newStr, candidates);
        }
    }
}
