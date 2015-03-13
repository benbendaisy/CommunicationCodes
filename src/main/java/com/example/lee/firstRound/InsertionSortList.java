package com.example.lee.firstRound;

import com.example.lee.model.ListNode;

/**
 * Created by pzhong1 on 12/16/14.
 * Sort a linked list using insertion sort.
 */
public class InsertionSortList {
    public ListNode insertionSortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode prev = head;
        ListNode current = head.next;
        ListNode previous = new ListNode(0);
        previous.next = head;
        head = previous;
        while(current != null){
            previous = head;
            ListNode start = previous.next;
            while(start != null && start != current){
                if(start.val > current.val){
                    previous.next = current;
                    ListNode temp = current.next;
                    current.next = start;
                    current = prev;
                    prev.next = temp;
                    break;
                }
                previous = start;
                start = start.next;
            }
            prev = current;
            current = current.next;
        }
        return head.next;
    }
}
