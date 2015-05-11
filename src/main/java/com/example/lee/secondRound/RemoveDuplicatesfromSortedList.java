package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 5/4/15.
 */
public class RemoveDuplicatesfromSortedList {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode prev = dummyHead, cur = head;
        int pNum = Integer.MAX_VALUE;
        while (cur != null) {
            if (pNum == cur.val) {
                prev.next = cur.next;
                cur.next = null;
                cur = prev.next;
            } else {
                pNum = cur.val;
                prev = cur;
                cur = cur.next;
            }
        }
        return dummyHead.next;
    }
}
