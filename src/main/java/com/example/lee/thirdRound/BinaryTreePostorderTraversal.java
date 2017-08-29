package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.*;

public class BinaryTreePostorderTraversal {
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) {
            return Collections.emptyList();
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        List<Integer> list = new ArrayList<>();
        Set<TreeNode> visited = new HashSet<>();
        while (!stack.isEmpty()) {
            // check if we already handled its childrens
            if (!visited.add(stack.peek())) {
                TreeNode node = stack.pop();
                list.add(node.val);
            } else {
                TreeNode node = stack.peek();
                // handling right child
                if (node.right != null) {
                    stack.push(node.right);
                }
                // handling left child
                if (node.left !=  null) {
                    stack.push(node.left);
                }
            }
        }
        return list;
    }
}
