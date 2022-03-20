package com.example.lee.firstRound;

import com.example.lee.model.TreeLinkNode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by benbendaiy on 1/1/15.
 * Follow up for problem "Populating Next Right Pointers in Each Node".
 * What if the given tree could be any binary tree? Would your previous solution still work?
 * Note:
 *
 * You may only use constant extra space.
 * For example,
 * Given the following binary tree,
 * 1
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
        if(root == null){
            return;
        }
        Queue<TreeLinkNode> queue1 = new LinkedList<TreeLinkNode>();
        Queue<TreeLinkNode> queue2 = new LinkedList<TreeLinkNode>();
        queue1.add(root);
        TreeLinkNode prev = null;
        while(!queue1.isEmpty()){
            TreeLinkNode node = queue1.poll();
            if(node.left != null){
                queue2.add(node.left);
                if(prev != null){
                    prev.next = node.left;
                }

                prev = node.left;
            }
            if(node.right != null){
                queue2.add(node.right);
                if(prev != null){
                    prev.next = node.right;
                }
                prev = node.right;
            }
            if(queue1.isEmpty()){
                node.next = null;
                prev = null;
            }
            if(queue1.isEmpty() && !queue2.isEmpty()){
                queue1 = queue2;
                queue2 = new LinkedList<TreeLinkNode>();
            }
        }
    }

    //recursive way
    public void connectI(TreeLinkNode root) {
        if(root == null){
            return;
        }
        if(root.right != null){
            root.right.next = findNext(root.next);
            connect(root.right);
        }

        if(root.left != null){
            root.left.next = root.right == null ? findNext(root.next) : root.right;
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
