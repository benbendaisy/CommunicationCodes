package com.example.lee;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 12/22/14.
 * Given a singly linked list L: L0→L1→…→Ln-1→Ln,
 * reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
 * You must do this in-place without altering the nodes' values.
 * For example,
 * Given {1,2,3,4}, reorder it to {1,4,2,3}.
 */
public class ReorderList {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null){
            return;
        }
        ListNode current = head;
        ListNode runner = head;
        ListNode prev = new ListNode(0);
        prev.next = current;
        while(runner != null && runner.next != null){
            prev.next = current;
            prev = prev.next;
            current = current.next;
            runner = runner.next.next;
        }

        runner = current;
        while(runner != null){
            ListNode temp = runner.next;
            runner.next = prev;
            prev = runner;
            runner = temp;
        }

        while(prev != current){
            ListNode temp = head.next;
            head.next = prev;
            ListNode temp1 = prev.next;
            prev.next = temp;
            prev = temp1;
            head = temp;
        }
        current.next = null;
    }

    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        node1.next = node2;
        node2.next = node3;
        ReorderList reorderList = new ReorderList();
        reorderList.reorderList(node1);
        reorderList.printAll(node1);
    }

    public void printAll(ListNode node){
        while(node != null){
            System.out.println(node.val);
            node = node.next;
        }
    }
}
