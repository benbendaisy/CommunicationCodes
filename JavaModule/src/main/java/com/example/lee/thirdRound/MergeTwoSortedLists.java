package com.example.lee.thirdRound;

import java.util.List;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class MergeTwoSortedLists {
     // Definition for singly-linked list.
     private static class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
     }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        }
        ListNode prev = new ListNode(0);
        ListNode cur = prev;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
        if (l1 != null) {
            cur.next = l1;
        } else {
            cur.next = l2;
        }
        return prev.next;
    }
}
