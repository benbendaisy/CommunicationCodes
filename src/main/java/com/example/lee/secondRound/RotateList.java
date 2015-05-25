package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 5/18/15.
 *
 * Given a list, rotate the list to the right by k places, where k is non-negative.
 *
 * For example:
 * Given 1->2->3->4->5->NULL and k = 2,
 * return 4->5->1->2->3->NULL.
 *
 */
public class RotateList {
    public ListNode rotateRight(ListNode head, int k) {
        if (null == head || k <= 0) return head;
        ListNode dummyHead = new ListNode(-1);
        dummyHead.next = head;
        ListNode cur = head;
        int len = 0;
        while (null != cur) {
            cur = cur.next;
            len++;
        }
        k = k % len;
        if (k == 0) return head;
        cur = head;
        while (k > 0 && null != cur) {
            cur = cur.next;
            k--;
        }
        if (null == cur) return head;
        ListNode prev = head;
        while (null != cur.next) {
            prev = prev.next;
            cur = cur.next;
        }
        dummyHead.next = prev.next;
        prev.next = null;
        cur.next = head;
        return dummyHead.next;
    }

    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        node1.next = node2;
        node2.next = node3;
        RotateList rotateList = new RotateList();
        ListNode head = rotateList.rotateRight(node1, 20000);
        System.out.println(head.val);
    }
}
