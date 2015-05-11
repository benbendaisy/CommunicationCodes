package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 5/3/15.
 */
public class PrintMaximumNumberofAsUsingGivenFourKeys {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode prev = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        PrintMaximumNumberofAsUsingGivenFourKeys pmm = new PrintMaximumNumberofAsUsingGivenFourKeys();
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        node1.next = node2;
        System.out.println(pmm.reverseList(node1).val);
    }
}
