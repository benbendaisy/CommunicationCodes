package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class RecoverBinarySearchTree {
    private TreeNode node1 = null, node2 = null, prev = null;
    public void recoverTreeI(TreeNode root) {
        if (root == null) {
            return;
        }
        findNodes(root);
        if (node1 == null || node2 == null) {
            return;
        }
        int t = node1.val;
        node1.val = node2.val;
        node2.val = t;
    }

    private void findNodes(TreeNode root) {
        if (root == null) {
            return;
        }
        findNodes(root.left);
        if (prev != null && prev.val > root.val) {
            if (node1 == null) {
                node1 = prev; // in case they are neighbors
                node2 = root;
            } else {
                node2 = root;
                return;
            }
        }
        prev = root;
        findNodes(root.right);
    }

    public void recoverTree(TreeNode root) {
        if (root == null) {
            return;
        }

        List<TreeNode> list = new ArrayList<>();
        recoverTreeHelper(root, list);
        int l = 0, r = list.size() - 1;
        while (l < list.size() - 1) {
            if (list.get(l).val > list.get(l + 1).val) {
                break;
            }
            l++;
        }

        while (r > 0) {
            if (list.get(r).val < list.get(r - 1).val) {
                break;
            }
            r--;
        }

        int t = list.get(l).val;
        list.get(l).val = list.get(r).val;
        list.get(r).val = t;
    }

    private void recoverTreeHelper(TreeNode root, List<TreeNode> list) {
        if (root == null) {
            return;
        }
        recoverTreeHelper(root.left, list);
        list.add(root);
        recoverTreeHelper(root.right, list);
    }

    public static void main(String[] args) {
        RecoverBinarySearchTree recoverBinarySearchTree = new RecoverBinarySearchTree();
        TreeNode node1 = new TreeNode(0);
        TreeNode node2 = new TreeNode(1);
        node1.left = node2;
        recoverBinarySearchTree.recoverTreeI(node1);
    }
}
