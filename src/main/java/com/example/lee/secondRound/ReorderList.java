package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 3/28/15.
 */
public class ReorderList {
    public void reorderList(ListNode head) {
        if (null == head || null == head.next) return;
        ListNode runner = head, cur = head, prev = null;
        while (null != runner && null != runner.next) {
            prev = cur;
            cur = cur.next;
            runner = runner.next.next;
        }
        if (null != prev) {
            prev.next = null;
            prev = null;
        }
        while (null != cur) {
            ListNode t = cur.next;
            cur.next = prev;
            prev = cur;
            cur = t;
        }
        cur = prev;
        ListNode node = head;
        prev = head;
        while (null != node && null != cur) {
            ListNode next1 = node.next;
            ListNode next2 = cur.next;
            node.next = cur;
            cur.next = next1;
            prev = cur;
            node = next1;
            cur = next2;
        }

        if (null != cur) prev.next = cur;
    }

    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        node1.next = node2;
        node2.next = node3;
        ReorderList reorderList = new ReorderList();
        reorderList.reorderList(node1);
    }
}
