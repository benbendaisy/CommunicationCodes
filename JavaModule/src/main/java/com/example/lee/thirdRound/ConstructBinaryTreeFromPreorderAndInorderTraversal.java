package com.example.lee.thirdRound;

import com.example.lee.model.TreeNode;

import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ConstructBinaryTreeFromPreorderAndInorderTraversal {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length != inorder.length) {
            return null;
        }
        Map<Integer, Integer> indexMap2 = IntStream.range(0, inorder.length)
                .mapToObj(idx -> idx)
                .collect(Collectors.toMap(idx -> inorder[idx], Function.identity()));
        return buildTreeHelper(preorder,0, preorder.length - 1, inorder, 0, indexMap2);
    }

    private TreeNode buildTreeHelper(int[] preorder, int startIdx, int endIdx,
                                     int[] inorder, int startIdx1, Map<Integer, Integer> indxMap2) {
        if (startIdx > endIdx) {
            return null;
        }
        TreeNode node = new TreeNode(preorder[startIdx]);
        int idx = indxMap2.get(preorder[startIdx]);
        node.left = buildTreeHelper(preorder, startIdx + 1, startIdx + idx - startIdx1, inorder, startIdx1, indxMap2);
        node.right = buildTreeHelper(preorder, startIdx + idx - startIdx1 + 1, endIdx, inorder, idx + 1, indxMap2);
        return node;
    }

    public static void main(String[] args) {
        int[] preorder = {1, 2, 3};
        int[] inorder = {2, 1, 3};
        ConstructBinaryTreeFromPreorderAndInorderTraversal constructBinaryTreeFromPreorderAndInorderTraversal =
                new ConstructBinaryTreeFromPreorderAndInorderTraversal();
        TreeNode root = constructBinaryTreeFromPreorderAndInorderTraversal.buildTree(preorder, inorder);
        System.out.println();
    }
}
