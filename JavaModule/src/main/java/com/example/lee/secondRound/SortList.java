package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 3/23/15.
 */
public class SortList {
    //merge sort
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        return mergeSort(head);
    }

    private ListNode mergeSort(ListNode head){
        if(null == head || null == head.next){
            return head;
        }
        ListNode cur = head, runner = head;
        ListNode prev = new ListNode(0);
        prev.next = cur;
        while (runner != null && runner.next != null) {
            cur = cur.next;
            prev = prev.next;
            runner = runner.next.next;
        }

        prev.next = null;
        ListNode left = mergeSort(head);
        ListNode right = mergeSort(cur);
        return merge(left, right);
    }

    private ListNode merge(ListNode left, ListNode right) {
        if (null == left) {
            return left;
        } else if (null == right) {
            return right;
        }

        ListNode dummyHead = new ListNode(0);
        ListNode prev = dummyHead;
        while (null != left && null != right) {
            if (left.val < right.val) {
                prev.next = left;
                left = left.next;
            } else {
                prev.next = right;
                right = right.next;
            }
            prev = prev.next;
        }

        while (null != left) {
            prev.next = left;
            left = left.next;
            prev = prev.next;
        }

        while (null != right) {
            prev.next = right;
            right = right.next;
            prev = prev.next;
        }

        return dummyHead.next;
    }

    //quick sort cannot pass big tests
    public ListNode sortListI(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }
        sortListHelp(head, null);
        return head;
    }

    private void sortListHelp(ListNode head, ListNode end) {
        if (null == head || head == end) return;
        ListNode anchor = partition(head, end);
        sortListHelp(head, anchor);
        sortListHelp(anchor.next, end);
    }

    private ListNode partition(ListNode head, ListNode end) {
        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode lesser = head;
        ListNode bigger = head;

        while (lesser != end && bigger != end) {
            while (lesser != null && lesser != end && lesser.val <= head.val) {
                prev = prev.next;
                lesser = lesser.next;
            }
            while (bigger != null && bigger != end && bigger.val > head.val) {
                bigger = bigger.next;
            }
            if (bigger != null) {
                swap(lesser, bigger);
            }

        }
        swap(head, prev);
        return prev;
    }

    private void swap(ListNode node1, ListNode node2) {
        if (null != node1 && null != node2) {
            int t = node1.val;
            node1.val = node2.val;
            node2.val = t;
        }
    }
}
