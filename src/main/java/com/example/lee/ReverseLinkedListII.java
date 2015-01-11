package com.example.lee;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 1/9/15.
 *
 * Reverse a linked list from position m to n. Do it in-place and in one-pass.
 *
 * For example:
 * Given 1->2->3->4->5->NULL, m = 2 and n = 4,
 *
 * return 1->4->3->2->5->NULL.
 *
 * Note:
 * Given m, n satisfy the following condition:
 * 1 ≤ m ≤ n ≤ length of list.
 */
public class ReverseLinkedListII {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head == null || m == n){
            return head;
        }

        ListNode current = head;
        ListNode prev1 = new ListNode(0);
        prev1.next = current;
        int count = 1;
        while(current != null && count < m){
            prev1 = current;
            current = current.next;
            count++;
        }

        //reverse the link
        ListNode prev2 = prev1;
        while(current != null && m <= n){
            ListNode nodeTemp1 = current.next;
            current.next = prev2;
            prev2 = current;
            current = nodeTemp1;
            m++;
        }

        //keep the head if the head has been reversed
        if(prev1.next == head){
            head = prev2;
        }

        //link the first node to the last node that need to be reversed
        ListNode nodeTemp1 = prev1.next;
        prev1.next = prev2;
        nodeTemp1.next = current;

        return head;
    }

    public static void main(String[] args) {
        ReverseLinkedListII reverse = new ReverseLinkedListII();
        ListNode node = new ListNode(1);
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(3);
        node.next = node1;
        node1.next = node2;
        System.out.println(reverse.reverseBetween(node, 1, 3));
    }
}
