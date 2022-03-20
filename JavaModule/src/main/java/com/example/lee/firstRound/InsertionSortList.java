package com.example.lee.firstRound;

import com.example.lee.model.ListNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by pzhong1 on 12/16/14.
 * Sort a linked list using insertion sort.
 */
public class InsertionSortList {
    public ListNode insertionSortList(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode cur = head;
        ListNode previous = dummyHead;
        while (cur != null) {
            ListNode prev = dummyHead;
            while (prev.next != cur && prev.next.val < cur.val) {
                prev = prev.next;
            }
            if (prev.next != cur) {
                ListNode t = cur.next;
                cur.next = prev.next;
                prev.next = cur;
                cur = t;
                previous.next = t;
            } else {
                previous = cur;
                cur = cur.next;
            }
        }
        return dummyHead.next;
    }

    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();

    }
}
