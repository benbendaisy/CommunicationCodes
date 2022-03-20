package com.example.lee.firstRound;
import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 3/2/15.
 *
 * Given a linked list, remove the nth node from the end of list and return its head.
 *
 * For example,
 *
 * Given linked list: 1->2->3->4->5, and n = 2.
 *
 * After removing the second node from the end, the linked list becomes 1->2->3->5.
 * Note:
 * Given n will always be valid.
 * Try to do this in one pass.
 */
public class RemoveNthNodeFromEndofList {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (null == head) {
            return head;
        }
        ListNode cur = head, runner = head;
        ListNode prev = new ListNode(0);
        ListNode dummyHead = prev;
        prev.next = cur;

        while (n > 0 && null != runner) {
            runner = runner.next;
            n--;
        }

        while (runner != null) {
            cur = cur.next;
            runner = runner.next;
            prev = prev.next;
        }

        if (n == 0) {
            prev.next = cur.next;
        }

        return dummyHead.next;

    }
}
