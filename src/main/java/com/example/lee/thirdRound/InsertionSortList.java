package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

public class InsertionSortList {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummyHead = new ListNode(-1);
        dummyHead.next = head;
        ListNode cur = dummyHead;
        ListNode prev = dummyHead;
        ListNode runner = head;
        // 1 -> 2 -> 3
        while (runner != null) {
            while (cur != null && cur.next.val < runner.val) {
                cur = cur.next;
            }
            if (prev.next == cur.next) {
                prev = prev.next;
                runner = runner.next;
                cur = dummyHead;
                continue;
            }
            prev.next = runner.next;
            runner.next = cur.next;
            cur.next = runner;
            runner = prev.next;
            cur = dummyHead;
        }
        return dummyHead.next;
    }

    public static void main(String[] args) {
        InsertionSortList insertionSortList = new InsertionSortList();
        ListNode listNode1 = new ListNode(1);
        ListNode listNode2 = new ListNode(1);
        listNode1.next = listNode2;
        insertionSortList.insertionSortList(listNode1);
    }
}
