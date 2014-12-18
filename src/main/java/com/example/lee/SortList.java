package com.example.lee;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 12/17/14.
 * Sort a linked list in O(n log n) time using constant space complexity.
 * implement it by both quick sort and merge sort
 */
public class SortList {

    //quick sort
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        sortListHelp(head, null);
        return head;
    }

    private void sortListHelp(ListNode head, ListNode anchor){
        if(head == null || head == anchor){
            return;
        }
        ListNode partition = sortListPartition(head, anchor);
        sortListHelp(head, partition);
        sortListHelp(partition.next, anchor);
    }

    private ListNode sortListPartition(ListNode head, ListNode end){
        ListNode previous = new ListNode(0);
        previous.next = head;
        ListNode anchor = head;
        ListNode less = head;

        while(less != null && less != end && anchor.val >= less.val){
            previous = previous.next;
            less = less.next;
        }

        ListNode bigger = less;

        while(bigger != null && bigger != end){
            while(bigger != null && bigger != end && anchor.val < bigger.val){
                bigger = bigger.next;
            }
            if(bigger != null){
                swap(less, bigger);
                previous = previous.next;
                less = less.next;
                bigger = bigger.next;
            }
        }
        swap(anchor, previous);
        return previous;
    }

    private void swap(ListNode node1, ListNode node2){
        if(node1 != null && node2 != null){
            int temp = node1.val;
            node1.val = node2.val;
            node2.val = temp;
        }
    }

    //merge sort
    public ListNode sortList1(ListNode head) {
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
        first = sortList1(first);
        second = sortList1(second);
        return sortListMerge(first, second);
    }

    private ListNode sortListMerge(ListNode first, ListNode second){
        ListNode head = new ListNode(0);
        ListNode previous = head;
        while(first != null && second != null){
            while(first != null && second != null && first.val <= second.val){
                head.next = first;
                head = head.next;
                first = first.next;
            }

            while(second != null && first != null && second.val <= first.val){
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
