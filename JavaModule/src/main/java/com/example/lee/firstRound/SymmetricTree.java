package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by benbendaisy on 1/4/15.
 *
 * Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
 *
 * For example, this binary tree is symmetric:
 *
 *       1
 *      / \
 *     2   2
 *    / \ / \
 *   3  4 4  3
 * But the following is not:
 *       1
 *      / \
 *     2   2
 *     \   \
 *     3    3
 */
public class SymmetricTree {

    //iterative way
    public boolean isSymmetric(TreeNode root) {
        if(root == null || (root.left == null && root.right == null)){
            return true;
        } else if(root.left == null || root.right == null){
            return false;
        }

        Queue<TreeNode> queueL = new LinkedList<TreeNode>();
        Queue<TreeNode> queueR = new LinkedList<TreeNode>();
        queueL.add(root.left);
        queueR.add(root.right);
        while(!queueL.isEmpty() && !queueR.isEmpty()){
            TreeNode nodeL = queueL.poll();
            TreeNode nodeR = queueR.poll();
            if(nodeL.val != nodeR.val){
                return false;
            }

            if(nodeL.left != null && nodeR.right != null){
                queueL.add(nodeL.left);
                queueR.add(nodeR.right);
            } else if(nodeL.left != null || nodeR.right != null){
                return false;
            }

            if(nodeL.right != null && nodeR.left != null){
                queueL.add(nodeL.right);
                queueR.add(nodeR.left);
            } else if(nodeL.right != null || nodeR.left != null){
                return false;
            }


        }
        return queueL.isEmpty() && queueR.isEmpty();
    }

    //recursive way
    public boolean isSymmetricI(TreeNode root) {
        if(root == null || (root.left == null && root.right == null)){
            return true;
        }

        return isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode p, TreeNode q){
        if(p == null && q == null){
            return true;
        } else if(p == null || q == null){
            return false;
        }

        if(p.val != q.val){
            return false;
        } else {
            return isSymmetric(p.left, q.right) && isSymmetric(p.right, q.left);
        }
    }
}
