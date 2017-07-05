package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 7/1/17.
 */
public class SwapNodesinPairs {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode prev = new ListNode(0);
        ListNode cur = prev;
        cur.next = head;
        while (cur != null && cur.next != null && cur.next.next != null) {
            ListNode temp = cur.next;
            ListNode next = temp.next;
            temp.next = next.next;
            next.next = temp;
            cur.next = next;
            cur = temp;
        }
        return prev.next;
    }
}
