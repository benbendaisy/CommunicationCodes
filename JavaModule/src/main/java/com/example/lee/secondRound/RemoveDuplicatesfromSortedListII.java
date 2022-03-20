package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 5/4/15.
 */
public class RemoveDuplicatesfromSortedListII {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dHead = new ListNode(0);
        dHead.next = head;
        ListNode cur = head;
        ListNode pPrev = new ListNode(0);
        pPrev.next = dHead;
        int pNum = Integer.MIN_VALUE;
        while (cur != null) {
            if (pNum == cur.val) {
                while (cur != null && cur.val == pNum) {
                    cur = cur.next;
                }
                pPrev.next = cur;
                if (cur != null) {
                    pNum = cur.val;
                    cur = cur.next;
                }
            } else {
                pPrev = pPrev.next;
                pNum = cur.val;
                cur = cur.next;
            }
        }
        return dHead.next;
    }
}
