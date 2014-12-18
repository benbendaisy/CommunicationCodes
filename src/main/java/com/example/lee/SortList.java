package com.example.lee;

import com.example.lee.model.ListNode;

/**
 * Created by pzhong1 on 12/17/14.
 */
public class SortList {
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        } else if(head.next.next == null){
            ListNode temp = head.next;
            head.next = null;
            return sortListMerge(head, temp);
        }

        ListNode first = head, second = head;
        ListNode runner = head;
        ListNode prev = new ListNode(0);
        prev.next = second;
        while(second != null && runner != null && runner.next != null){
            second = second.next;
            prev = prev.next;
            runner = runner.next.next;
        }
        prev.next = null;
        first = sortList(first);
        second = sortList(second);
        return sortListMerge(first, second);
    }

    private ListNode sortListMerge(ListNode first, ListNode second){
        ListNode head = new ListNode(0);
        ListNode previous = head;
        while(first != null && second != null){
            while(first != null && second != null && first.val < second.val){
                head.next = first;
                head = head.next;
                first = first.next;
            }

            while(second != null && first != null && second.val < first.val){
                head.next = second;
                head = head.next;
                second = second.next;
            }
        }

        while(first != null){
            head.next = first;
            head = head.next;
            first = first.next;
        }

        while(second != null){
            head.next = second;
            head = head.next;
            second = second.next;
        }

        return previous.next;
    }

    public void printAll(ListNode head){
        while(head != null){
            System.out.print(head.val);
            System.out.print(",  ");
            head = head.next;
        }
    }
    public static void main(String[] args) {
        SortList sortList = new SortList();
        ListNode node1 = new ListNode(4);
        ListNode node2 = new ListNode(19);
        ListNode node3 = new ListNode(14);
        ListNode node4 = new ListNode(5);
        ListNode node5 = new ListNode(-3);
        ListNode node6 = new ListNode(1);
        ListNode node7 = new ListNode(8);
        ListNode node8 = new ListNode(5);
        ListNode node9 = new ListNode(11);
        ListNode node10 = new ListNode(15);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;
        node5.next = node6;
        node6.next = node7;
        node7.next = node8;
        node8.next = node9;
        node9.next = node10;
        node1 = sortList.sortList(node1);
        sortList.printAll(node1);
    }
}
