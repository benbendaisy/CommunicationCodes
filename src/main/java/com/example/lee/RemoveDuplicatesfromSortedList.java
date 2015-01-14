package com.example.lee;

import com.example.lee.model.ListNode;
/**
 * Created by benbendaisy on 1/12/15.
 *
 * Given a sorted linked list, delete all duplicates such that each element appear only once.
 *
 * For example,
 * Given 1->1->2, return 1->2.
 * Given 1->1->2->3->3, return 1->2->3.
 */
public class RemoveDuplicatesfromSortedList {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode prev = new ListNode(0);
        prev.next = head;

        ListNode prevCurrent = prev;
        ListNode current = head;
        while(current != null){
            while(current.next != null && current.val == current.next.val){
                current = current.next;
            }
            prevCurrent.next = current;
            prevCurrent = current;
            if(current != null){
                current = current.next;
            }
        }
        prevCurrent.next = null;

        return prev.next;
    }
}
