package com.example.lee.firstRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 2/26/15.
 *
 * Given a linked list, swap every two adjacent nodes and return its head.
 *
 * For example,
 * Given 1->2->3->4, you should return the list as 2->1->4->3.
 *
 * Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
 */
public class SwapNodesinPairs {
    public ListNode swapPairs(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }
        int n = 0;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode prev = dummyHead;
        ListNode cur = head;
        while (null != cur) {
            n++;
            if (n % 2 == 0) {
                prev = groupReverse(prev, cur.next);
                cur = prev.next;
            } else {
                cur = cur.next;
            }
        }
        return dummyHead.next;
    }

    private ListNode groupReverse(ListNode start, ListNode end) {
        ListNode prev = start.next;
        ListNode cur = prev.next;
        while (cur != end) {
            prev.next = cur.next;
            cur.next = start.next;
            start.next = cur;
            cur = prev.next;
        }
        return prev;
    }
}
