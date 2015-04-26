package com.example.lee.secondRound;

import com.example.lee.model.ListNode;
import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 4/14/15.
 */
public class ConvertSortedListtoBinarySearchTree {
    public TreeNode sortedListToBST(ListNode head) {
        if (null == head) {
            return null;
        } else if (null == head.next) {
            TreeNode n = new TreeNode(head.val);
            return n;
        }
        ListNode prev = new ListNode(0);
        ListNode cur = head, runner = head;
        prev.next = cur;
        while (null != runner && null != runner.next) {
            prev = cur;
            cur = cur.next;
            runner = runner.next.next;
        }
        ListNode nxt = cur.next;
        cur.next = null;
        prev.next = null;
        TreeNode node = new TreeNode(cur.val);
        node.left = sortedListToBST(head);
        node.right = sortedListToBST(nxt);
        return node;
    }

    public static void main(String[] args) {
        ListNode list = new ListNode(1);
        ListNode list1 = new ListNode(2);
        list.next = list1;
        ConvertSortedListtoBinarySearchTree csl= new ConvertSortedListtoBinarySearchTree();
        csl.sortedListToBST(list);
    }
}
