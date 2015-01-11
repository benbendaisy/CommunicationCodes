package com.example.lee;

import com.example.lee.model.ListNode;
/**
 * Created by benbendaisy on 1/10/15.
 *
 * Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
 *
 * You should preserve the original relative order of the nodes in each of the two partitions.
 *
 * For example,
 * Given 1->4->3->2->5->2 and x = 3,
 * return 1->2->2->4->3->5.
 */
public class PartitionList {
    public ListNode partition(ListNode head, int x) {
        if(head == null || head.next == null){
            return head;
        }

        ListNode leftFirst = new ListNode(0);
        ListNode rightFirst = new ListNode(0);
        ListNode current = head;
        ListNode left = head, right = head;
        boolean isLeftFirst = true;
        boolean isRightFirst = true;
        while(current != null){
            if(current.val < x){
                if(isLeftFirst){
                    isLeftFirst = false;
                    leftFirst.next = current;
                } else {
                    left.next = current;
                }
                left = current;
            } else {
                if(isRightFirst){
                    isRightFirst = false;
                    rightFirst.next = current;
                } else {
                    right.next = current;
                }
                right = current;
            }
            ListNode next = current.next;
            current.next = null;
            current = next;
        }
        if(leftFirst.next != null){
            left.next = rightFirst.next;
            return leftFirst.next;
        } else {
            return rightFirst.next;
        }
    }
}
