package com.example.lee.firstRound;

import com.example.lee.model.TreeLinkNode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by benbendaisy on 1/1/15.
 */
public class PopulatingNextRightPointersinEachNode {
    public void connect(TreeLinkNode root) {
        if(root == null){
            return;
        }
        Queue<TreeLinkNode> queue1 = new LinkedList<TreeLinkNode>();
        Queue<TreeLinkNode> queue2 = new LinkedList<TreeLinkNode>();
        queue1.add(root);
        TreeLinkNode prev = null;
        while(!queue1.isEmpty()){
            TreeLinkNode node = queue1.poll();
            if(node.left != null && node.right != null){
                queue2.add(node.left);
                queue2.add(node.right);

                //if node.left is not null then node.right must not be null
                node.left.next = node.right;
                if(prev != null){
                    prev.next = node.left;
                }

                prev = node.right;
                if(queue1.isEmpty()){
                    node.next = null;
                }
            }


            if(queue1.isEmpty() && !queue2.isEmpty()){
                queue1 = queue2;
                queue2 = new LinkedList<TreeLinkNode>();
            }
        }

    }

    //recursive way. notice: if root.left is not null then root.right is not null.
    //reverse is the same
    public void connectI(TreeLinkNode root) {
        if(root == null){
            return;
        }
        if(root.right != null){
            root.left.next = root.right;
            root.right.next = findNext(root.next);
            connect(root.right);
            connect(root.left);
        }
    }

    private TreeLinkNode findNext(TreeLinkNode root){
        while(root != null && root.left == null && root.right == null){
            root = root.next;
        }

        if(root != null){
            return root.left == null ? root.right : root.left;
        }

        return null;
    }
}
