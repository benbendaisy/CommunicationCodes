package com.example.lee.firstRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 2/26/15.
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
public class ReverseNodesinKGroup {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (null == head || k == 1) {
            return head;
        }
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode prev = dummyHead, cur = head;
        int n = 0;
        while (null != cur) {
            n++;
            if (n % k == 0) {
                prev = reverseList(prev, cur.next);
                cur = prev.next;
            } else {
                cur = cur.next;
            }
        }
        return dummyHead.next;
    }

    private ListNode reverseList(ListNode start, ListNode end) {
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

    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        ReverseNodesinKGroup reverseNodesinKGroup = new ReverseNodesinKGroup();

        //System.out.println(reverseNodesinKGroup.reverseKGroup(node1, 2).val);
        ListNode head = new ListNode(0);
        head.next = node1;
        node1 = node2;

        System.out.println(head.next.val);

    }
}
