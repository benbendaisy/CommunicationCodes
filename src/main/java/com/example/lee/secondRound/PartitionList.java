package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 5/1/15.
 *
 * Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
 *
 * You should preserve the original relative order of the nodes in each of the two partitions.
 *
 * For example,
 * Given 1->4->3->2->5->2 and x = 3,
 * return 1->2->2->4->3->5.
 */
public class PartitionList {
    public ListNode partition(ListNode head, int x) {
        if (null == head || null == head.next) return head;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode prev = dummyHead;
        while (head != null && head.val < x) {
            prev = head;
            head = head.next;
        }
        ListNode prev1 = head;
        if (head != null && head.next != null) {
            ListNode cur = head.next;
            while (cur != null) {
                if (cur.val < x) {
                    moveNode(prev, prev1);
                    cur = prev1;
                    prev = prev.next;
                } else {
                    prev1 = cur;
                    cur = cur.next;
                }
            }
        }
        return dummyHead.next;
    }

    private void moveNode(ListNode prev1, ListNode prev2) {
        ListNode next1 = prev1.next;
        ListNode cur = prev2.next;
        prev1.next = cur;
        prev2.next = cur.next;
        cur.next = next1;
    }
}
