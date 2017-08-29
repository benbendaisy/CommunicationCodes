package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

public class ReorderList {
    /**
     * basic idea:
     * 1, find the middle node
     * 2, reverse all the node after middle node
     * 3, set middle node's next to null to break the link
     * 4, insert all the nodes after middle nodes to first part
     * @param head
     */
    public void reorderList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return;
        }

        ListNode cur = head;
        int cnt = 0;
        while (cur != null) {
            cnt++;
            cur = cur.next;
        }

        cur = head;
        int half = (cnt - 1) / 2;
        while (half > 0) {
            cur = cur.next;
            half--;
        }
        //reverse the node after runner
        ListNode last = cur.next;
        if (last == null) {
            return;
        }
        ListNode next = last.next;
        while (next != null) {
            last.next = next.next;
            next.next = cur.next;
            cur.next = next;
            next = last.next;
        }

        ListNode prev = head;
        ListNode runner = cur.next;
        cur.next = null;
        while (runner != null) {
            ListNode t1 = runner.next;
            runner.next = prev.next;
            prev.next = runner;
            runner = t1;
            prev = prev.next.next;
        }
    }
    /**
     *  1 -> 2 -> 3
     *  1 -> 2 -> 3 <- 4
     * @param head
     */
    public void reorderListI(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }

        ListNode cur = head;
        ListNode runner = head;
        while (runner != null && runner.next != null) {
            cur = cur.next;
            runner = runner.next.next;
        }

        ListNode end = cur.next;
        // reverse the rest of link
        runner = cur.next;
        while (runner != null) {
            ListNode t = runner.next;
            runner.next = cur;
            cur = runner;
            runner = t;
        }

        runner = head;
        while (runner.next != end) {
            ListNode t = runner.next;
            if (t == cur) {
                break;
            }
            runner.next = cur;
            cur = cur.next;
            runner = runner.next;
            runner.next = t;
            runner = runner.next;
        }
    }

    public static void main(String[] args) {
        ReorderList reorderList = new ReorderList();
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
//        ListNode node4 = new ListNode(4);
        node1.next = node2;
        node2.next = node3;
//        node3.next = node4;
        reorderList.reorderList(node1);
    }
}
