package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.*;

/**
 * Created by benbendaisy on 3/26/15.
 */
public class BinaryTreePostorderTraversal {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        postorderTraversal(root, list);
        return list;
    }

    public void postorderTraversal(TreeNode root, List<Integer> list) {
        if (null == root) return;
        if (null != root.left) postorderTraversal(root.left, list);
        if (null != root.right) postorderTraversal(root.right, list);
        list.add(root.val);
    }

    public List<Integer> postorderTraversalI(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> list = new ArrayList<Integer>();
        if (null == root) return list;
        Set<TreeNode> set = new HashSet<TreeNode>();
        TreeNode node = root;
        while (null != node) {
            stack.add(node);
            node = node.left;
        }

        while (!stack.isEmpty()) {
            node = stack.peek();
            if (null == node.right || !set.add(node)) {
                list.add(node.val);
                stack.pop();
            } else {
                set.add(node);
                node = node.right;
                while (null != node) {
                    stack.push(node);
                    node = node.left;
                }
            }
        }
        return list;
    }

    public List<Integer> postorderTraversalII(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> list = new ArrayList<Integer>();
        if (null == root) return list;
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (null != node.right) {
                TreeNode right = node.right;
                TreeNode left = node.left;
                stack.push(node);
                stack.push(right);
                node.right = null;
                if (null != left) {
                    stack.push(left);
                    node.left = null;
                }
            } else if (null != node.left) {
                stack.push(node);
                stack.push(node.left);
                node.left = null;
            } else {
                list.add(node.val);
            }
        }
        return list;
    }

    public static void main(String[] args) {
        //test replace
        String str = "a b c";
        System.out.println(str.replace(' ', '_'));
        System.out.println(str.replaceAll(" ", "_"));
        System.out.println(str.replaceAll("\\s", "_"));

        str = "a     b    c";
        System.out.println(str.replaceAll(" +", "_"));
        System.out.println(str.replaceAll("[ ]+", "_"));
        System.out.println(str.replaceAll("\\s+", "_"));

        BinaryTreePostorderTraversal binaryTreePostorderTraversal = new BinaryTreePostorderTraversal();
        TreeNode root = new TreeNode(1);
        TreeNode node = new TreeNode(2);
        root.right = node;

        //thread safe sync list
        List syncList = Collections.synchronizedList(new ArrayList());

        //thread safe sync set
        Set syncSet = Collections.synchronizedSet(new HashSet());

        System.out.println(binaryTreePostorderTraversal.postorderTraversalI(root));

    }
}
