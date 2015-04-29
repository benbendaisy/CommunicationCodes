package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 4/27/15.
 *
 * Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
 *
 * If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
 *
 * You may not alter the values in the nodes, only nodes itself may be changed.
 *
 * Only constant memory is allowed.
 *
 * For example,
 * Given this linked list: 1->2->3->4->5
 *
 * For k = 2, you should return: 2->1->4->3->5
 *
 * For k = 3, you should return: 3->2->1->4->5
 */
public class ReverseNodesinkGroup {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (null == head || k == 1) return head;
        int n = 0;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode cur = head;
        ListNode start = dummyHead;
        while (null != cur) {
            n++;
            if(n % k == 0) {
                start = reverseKGroup(start, cur.next);
                cur = start.next;
            } else {
                cur = cur.next;
            }
        }
        return dummyHead.next;
    }

    private ListNode reverseKGroup(ListNode start, ListNode end) {
        ListNode last = start.next;
        ListNode cur = last.next;
        while (cur != end) {
            last.next = cur.next;
            cur.next = start.next;
            start.next = cur;
            cur = last.next;
        }
        return last;
    }
}
