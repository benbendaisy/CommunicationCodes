package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 6/23/15.
 *
 * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 *
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (null == l1) return l2;
        if (null == l2) return l1;
        ListNode dummyHead = new ListNode(-1);
        ListNode prev = dummyHead;
        int carr = 0;
        while (l1 != null && l2 != null) {
            int val = l1.val + l2.val + carr;
            int num = val % 10;
            carr = val / 10;
            prev.next = new ListNode(num);
            prev = prev.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        while (l1 != null) {
            int val = l1.val + carr;
            int num = val % 10;
            carr = val / 10;
            prev.next = new ListNode(num);
            prev = prev.next;
            l1 = l1.next;
        }

        while (l2 != null) {
            int val = l2.val + carr;
            int num = val % 10;
            carr = val / 10;
            prev.next = new ListNode(num);
            prev = prev.next;
            l2 = l2.next;
        }

        if (carr != 0) prev.next = new ListNode(carr);

        return dummyHead.next;
    }
}
