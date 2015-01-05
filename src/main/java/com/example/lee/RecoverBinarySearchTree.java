package com.example.lee;

import apple.laf.JRSUIUtils;
import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/4/15.
 *
 * Two elements of a binary search tree (BST) are swapped by mistake.
 *
 * Recover the tree without changing its structure.
 *
 * Note:
 * A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
 * refer to http://blog.csdn.net/fightforyourdream/article/details/16875941
 *
 */
public class RecoverBinarySearchTree {
    private TreeNode node1 = null, node2 = null, prev = null;

    ////o(1) space solution
    public void recoverTree(TreeNode root) {
        if(root == null){
            return;
        }
        findNodes(root);
        if(node1 != null && node2 != null){
            int val = node1.val;
            node1.val = node2.val;
            node2.val = val;
        }
    }

    private void findNodes(TreeNode root){
        if(root == null){
            return;
        }
        findNodes(root.left);
        if(prev == null){
            prev = root;
        } else if(prev.val > root.val){
            if(node1 == null){
                node1 = prev; //assume two nodes that are not in oders are neighbors
                node2 = root;
            } else {
                node2 = root; //find another one not in order and should be the smaller
                return;
            }
        }
        prev = root;
        findNodes(root.right);
    }

    //o(n) space solution
    public void recoverTreeI(TreeNode root) {
        if(root == null){
            return;
        }
        List<TreeNode> lt = new ArrayList<TreeNode>();
        inOrder(root, lt);
        TreeNode node1 = null, node2 = null; //save two nodes are not in orders
        if(lt.size() >= 2){
            TreeNode prev = lt.get(0);
            for(int i = 1; i < lt.size(); i++){
                if(prev.val > lt.get(i).val){
                    if(node1 == null){
                        node1 = prev;
                        node2 = lt.get(i); //assume two nodes that are not in oders are neighbors
                    } else {
                        node2 = lt.get(i); //find another one not in order and should be the smaller
                        break;
                    }
                }
                prev = lt.get(i);
            }
            if(node1 != null && node2 != null){
                int val = node1.val;
                node1.val = node2.val;
                node2.val = val;
            }
        }
    }

    private void inOrder(TreeNode root, List<TreeNode> lt){
        if(root == null){
            return;
        }
        inOrder(root.left, lt);
        lt.add(root);
        inOrder(root.right, lt);
    }



    public static void main(String[] args) {
        RecoverBinarySearchTree recoverBinarySearchTree = new RecoverBinarySearchTree();
        TreeNode node1 = new TreeNode(2);
        TreeNode node2 = new TreeNode(3);
        TreeNode node3 = new TreeNode(1);
        node1.left = node2;
        node1.right = node3;
        recoverBinarySearchTree.recoverTree(node1);
    }
}
