package com.example.lee.firstRound;

import com.example.lee.model.TreeNode;
import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 1/3/15.
 *
 * Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
 */
public class ConvertSortedListtoBinarySearchTree {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode current = head;
        ListNode runner = head;
        ListNode prev = new ListNode(0);
        prev.next = current;
        while(runner != null && runner.next != null ){
            prev = current;
            current = current.next;
            runner = runner.next.next;
        }

        TreeNode node = new TreeNode(current.val);
        if(head != current){
            prev.next = null;
            node.left = sortedListToBST(head);
        }
        if(current.next != null){
            node.right = sortedListToBST(current.next);
        }
        return node;
    }

    public static void main(String[] args) {
        ConvertSortedListtoBinarySearchTree convert = new ConvertSortedListtoBinarySearchTree();
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(3);
        node1.next = node2;
        convert.sortedListToBST(node1);
    }
}
