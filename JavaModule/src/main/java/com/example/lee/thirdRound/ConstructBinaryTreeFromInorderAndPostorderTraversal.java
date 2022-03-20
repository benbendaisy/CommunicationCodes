package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ConstructBinaryTreeFromInorderAndPostorderTraversal {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder == null || inorder.length != postorder.length) {
            return null;
        }
        Map<Integer, Integer> idxMap = IntStream.range(0, inorder.length)
                .mapToObj(idx -> idx)
                .collect(Collectors.toMap(idx -> inorder[idx], Function.identity()));
        return buildTreeHelper(inorder, inorder.length - 1, idxMap, postorder, 0, postorder.length - 1);
    }

    private TreeNode buildTreeHelper(int[] inOrder, int endIdx1, Map<Integer, Integer> idxMap,
                                     int[] postOrder, int startIdx, int endIdx2) {
        if (startIdx > endIdx2) {
            return null;
        }
        TreeNode node = new TreeNode(postOrder[endIdx2]);
        int idx = idxMap.get(postOrder[endIdx2]);
        int len = endIdx1 - idx;
        node.left = buildTreeHelper(inOrder, idx - 1, idxMap, postOrder, startIdx, endIdx2 - len - 1);
        node.right = buildTreeHelper(inOrder, endIdx1, idxMap, postOrder, endIdx2 - len, endIdx2 - 1);
        return node;
    }

    public static void main(String[] args) {
        ConstructBinaryTreeFromInorderAndPostorderTraversal constructBinaryTreeFromInorderAndPostorderTraversal =
                new ConstructBinaryTreeFromInorderAndPostorderTraversal();
        int[] inOrder = {2, 1};
        int[] postOrder = {2, 1};
        TreeNode node = constructBinaryTreeFromInorderAndPostorderTraversal.buildTree(inOrder, postOrder);
        System.out.println();
    }
}
