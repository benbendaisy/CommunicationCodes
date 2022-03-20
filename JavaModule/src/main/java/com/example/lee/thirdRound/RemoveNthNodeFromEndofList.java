package com.example.lee.thirdRound;

import java.util.List;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class RemoveNthNodeFromEndofList {
    // Definition for singly-linked list.
    private static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }


    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
            return head;
        }
        ListNode prev = new ListNode(1);
        prev.next = head;
        ListNode cur1 = prev;
        ListNode cur2 = head;
        while (cur2 != null && n > 0) {
            cur2 = cur2.next;
            n--;
        }
        if (n > 0) {
            return head;
        }
        while (cur2 != null) {
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
        if (cur1.next != null) {
            cur1.next = cur1.next.next;
        }
        return prev.next;
    }
}
