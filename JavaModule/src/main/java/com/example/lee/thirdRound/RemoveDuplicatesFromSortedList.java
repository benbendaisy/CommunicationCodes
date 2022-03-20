package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 7/16/17.
 */
public class RemoveDuplicatesFromSortedList {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode dummyHead = new ListNode(-1);
        ListNode cur = head;
        ListNode end = dummyHead;
        while (cur != null) {
            while (cur.next != null && cur.val == cur.next.val) {
                cur = cur.next;
            }
            end.next = cur;
            end = end.next;
            cur = cur.next;
        }
        return dummyHead.next;
    }
}
