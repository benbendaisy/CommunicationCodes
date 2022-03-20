package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 4/27/15.
 *
 * Reverse a linked list from position m to n. Do it in-place and in one-pass.
 *
 * For example:
 * Given 1->2->3->4->5->NULL, m = 2 and n = 4,
 *
 * return 1->4->3->2->5->NULL.
 */
public class ReverseLinkedListII {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (null == head || m == n) return head;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode start = dummyHead, end = dummyHead;

        while (m > 1 && start != null) {
            start = start.next;
            m--;
        }

        while (n >= 0 && end != null) {
            end = end.next;
            n--;
        }

        ListNode last = start.next;
        ListNode cur = last.next;
        while (cur != end) {
            last.next = cur.next;
            cur.next = start.next;
            start.next = cur;
            cur = last.next;
        }
        return dummyHead.next;
    }

    public static void main(String[] args) {
        ReverseLinkedListII reverseLinkedListII = new ReverseLinkedListII();
        ListNode node1 = new ListNode(3);
        ListNode node2 = new ListNode(5);
        node1.next = node2;
        reverseLinkedListII.reverseBetween(node1, 1, 2);
        System.out.println("hello");
    }
}
