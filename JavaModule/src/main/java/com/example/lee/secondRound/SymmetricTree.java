package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by benbendaisy on 4/18/15.
 */
public class SymmetricTree {

    //iterative way
    public boolean isSymmetric(TreeNode root) {
        if (null == root || (null == root.left && null == root.right)) {
            return true;
        } else if (null == root.left || null == root.right || root.left.val != root.right.val) {
            return false;
        }

        Queue<TreeNode> queL = new LinkedList<TreeNode>();
        Queue<TreeNode> queR = new LinkedList<TreeNode>();
        queL.add(root.left);
        queR.add(root.right);
        while (!queL.isEmpty() && !queR.isEmpty()) {
            TreeNode nl = queL.poll();
            TreeNode nr = queR.poll();
            if (nl.val != nr.val) return false;
            if (null != nl.left && null != nr.right) {
                queL.add(nl.left);
                queR.add(nr.right);
            } else if (null != nl.left || null != nr.right) {
                return false;
            }

            if (null != nl.right && null != nr.left) {
                queL.add(nl.right);
                queR.add(nr.left);
            } else if (null != nl.right || null != nr.left) {
                return false;
            }
        }
        return queL.isEmpty() && queR.isEmpty();
    }

    public boolean isSymmetricI(TreeNode root) {
        if (null == root || (null == root.left && null == root.right)) {
            return true;
        } else if (null == root.left || null == root.right || root.left.val != root.right.val) {
            return false;
        } else {
            return isSymmetric(root.left, root.right);
        }
    }

    private boolean isSymmetric(TreeNode left, TreeNode right) {
        if (null == left && null == right) {
            return true;
        } else if (null == left || null == right || left.val != right.val) {
            return false;
        } else {
            return isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left);
        }
    }


}
