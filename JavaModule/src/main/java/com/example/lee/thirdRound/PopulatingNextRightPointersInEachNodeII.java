package com.example.lee.thirdRound;

import com.example.lee.model.TreeLinkNode;

public class PopulatingNextRightPointersInEachNodeII {
    public void connect(TreeLinkNode root) {
        if (root == null) {
            return;
        }
        TreeLinkNode node = getNextRight(root.next);
        if (root.right != null) {
            root.right.next = node;
            connect(root.right);
        }
        if (root.left != null) {
            if (root.right != null) {
                root.left.next = root.right;
            } else {
                root.left.next = node;
            }
            connect(root.left);
        }
    }

    private TreeLinkNode getNextRight(TreeLinkNode root) {
        if (root == null) {
            return null;
        } else if (root.left != null) {
            return root.left;
        } else if (root.right != null) {
            return root.right;
        } else {
            return getNextRight(root.next);
        }
    }
}
