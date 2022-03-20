package com.example.lee.firstRound;

import java.util.HashSet;
import java.util.Set;
import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
 *
 * For example,
 * Given 1->2->3->3->4->4->5, return 1->2->5.
 * Given 1->1->1->2->3, return 2->3.
 */
public class RemoveDuplicatesfromSortedListII {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode current = head;
        ListNode prevCurrent = prev;
        while (current != null) {
            if (current.next != null && current.val == current.next.val) {
                while(current.next != null && current.val == current.next.val){
                    current = current.next;
                }
            } else {
                prevCurrent.next = current;
                prevCurrent = current;
            }

            if(current != null){
                current = current.next;
            }
        }
        prevCurrent.next = null;
        return prev == prevCurrent ? null : prev.next;
    }
}
