package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 6/18/17.
 */
public class AddingTwoNumbers {
    private static class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        }
        int cur = (l1.val + l2.val) % 10;
        int carr = (l1.val + l2.val) / 10;
        ListNode newList = new ListNode(cur);
        ListNode prev = new ListNode(0);
        prev.next = newList;
        l1 = l1.next;
        l2 = l2.next;
        while (l1 != null && l2 != null) {
            int sum = l1.val + l2.val + carr;
            cur = sum % 10;
            carr = sum / 10;
            ListNode newListNode = new ListNode(cur);
            newList.next = newListNode;
            newList = newListNode;
            l1 = l1.next;
            l2 = l2.next;
        }
        while (l1 != null) {
            int sum = l1.val + carr;
            cur = sum % 10;
            carr = sum / 10;
            ListNode newListNode = new ListNode(cur);
            newList.next = newListNode;
            newList = newListNode;
            l1 = l1.next;
        }
        while (l2 != null) {
            int sum = l2.val + carr;
            cur = sum % 10;
            carr = sum / 10;
            ListNode newListNode = new ListNode(cur);
            newList.next = newListNode;
            newList = newListNode;
            l2 = l2.next;
        }
        if (carr != 0) {
            ListNode newListNode = new ListNode(carr);
            newList.next = newListNode;
            newList = newListNode;
        }
        return prev.next;
    }

    private static ListNode revertListNode(ListNode listNode) {
        ListNode prev = null;
        while (listNode != null) {
            ListNode nextNode = listNode.next;
            listNode.next = prev;
            prev = listNode;
            listNode = nextNode;
        }
        return prev;
    }

    public static void main(String[] args) {
        ListNode n1 = new ListNode(2);
        ListNode n2 = new ListNode(4);
        ListNode n3 = new ListNode(3);
        n1.next = n2;
        n2.next = n3;
        n1 = revertListNode(n1);
        while (n1 != null) {
            System.out.println(n1.val);
            n1 = n1.next;
        }
    }

}
