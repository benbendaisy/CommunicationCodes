package com.example.lee.secondRound;

import com.example.lee.model.TreeLinkNode;

/**
 * Created by benbendaisy on 4/12/15.
 *
 * Follow up for problem "Populating Next Right Pointers in Each Node".
 *
 * What if the given tree could be any binary tree? Would your previous solution still work?
 *
 * Note:
 *
 * You may only use constant extra space.
 * For example,
 * Given the following binary tree,
 *  1
 * /  \
 * 2    3
 * / \    \
 * 4   5    7
 * After calling your function, the tree should look like:
 * 1 -> NULL
 * /  \
 * 2 -> 3 -> NULL
 * / \    \
 * 4-> 5 -> 7 -> NULL
 */
public class PopulatingNextRightPointersinEachNodeII {
    public void connect(TreeLinkNode root) {
        if (null == root) return;
        if (null != root.right) {
            root.right.next = findNext(root.next);
            connect(root.right);
        }
        if (null != root.left) {
            root.left.next = root.right == null ? findNext(root.next) : root.right;
            connect(root.left);
        }
    }

    private TreeLinkNode findNext(TreeLinkNode root) {
        if (null == root) {
            return null;
        } else if (null != root.left) {
            return root.left;
        } else if (null != root.right) {
            return root.right;
        } else if (null != root.next) {
            return findNext(root.next);
        }
        return null;
    }
}
