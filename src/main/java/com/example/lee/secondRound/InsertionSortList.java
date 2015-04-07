package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 3/24/15.
 */
public class InsertionSortList {
    public ListNode insertionSortList(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode cur = head;
        while (cur != null) {
            ListNode prev = dummyHead;
            while (prev.next != cur && prev.next.val < cur.val) {
                prev = prev.next;
            }
            if (prev.next != cur) {
                ListNode t = cur.next;
                if (prev.next.next == cur) {
                    prev.next.next = cur.next;
                }
                //prev.next.next = cur.next;
                cur.next = prev.next;
                prev.next = cur;
                cur = t;
            } else {
                cur = cur.next;
            }
        }
        return dummyHead.next;
    }

    public static void main(String[] args) {
        InsertionSortList insertionSortList = new InsertionSortList();
        ListNode node1 = new ListNode(3);
        ListNode node2 = new ListNode(4);
        ListNode node3 = new ListNode(1);
        node1.next = node2;
        node2.next = node3;
        insertionSortList.insertionSortList(node1);
        System.out.println("te");
    }
}
