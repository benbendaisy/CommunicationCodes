package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

import java.util.List;

/**
 * Created by benbendaisy on 7/22/17.
 */
public class PartitionList {
    public ListNode partition(ListNode head, int x) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummyHead1 = new ListNode(-1);
        ListNode dummyHead2 = new ListNode(-1);
        dummyHead1.next = head;
        ListNode cur = head;
        ListNode prev = dummyHead1;
        ListNode cur2 = dummyHead2;
        while (cur != null) {
            if (cur.val <= x) {
                prev = cur;
                cur = cur.next;
            } else {
                cur2.next = cur;
                prev.next = cur.next;
                cur = cur.next;
                cur2 = cur2.next;
            }
        }
        cur2.next = null;
        prev.next = dummyHead2.next;
        return dummyHead1.next;
    }
    public ListNode partitionI(ListNode head, int x) {
        if (head == null) {
            return head;
        }
        ListNode dummyHead = new ListNode(-1);
        dummyHead.next = head;
        ListNode cur = head;
        while (cur != null && cur.val != x) {
            cur = cur.next;
        }

        if (cur == null) {
            return dummyHead.next;
        }

        ListNode node = cur;
        cur = cur.next;
        ListNode prev = dummyHead;
        while (cur != null) {
            if (cur.val < x) {
                prev = dummyHead;
                ListNode t = head;
                while (t.val <= x && t != node) {
                    prev = t;
                    t = t.next;
                }
                prev.next = cur; // -1 -> 1
                prev = cur; // prev = 1
                cur = cur.next; // cur = null
                prev.next = t; // 1 <=> 2
            } else {
                cur = cur.next;
            }
        }
        prev.next = null;
        return dummyHead.next;
    }




    public static void main(String[] args) {
        PartitionList partitionList = new PartitionList();
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(1);
        node1.next = node2;
        partitionList.partition(node1, 2);
    }
}
