package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;
import javafx.util.Pair;
import org.omg.PortableServer.LIFESPAN_POLICY_ID;

public class SortList {
    /**
     * this is going to implement merge sort
     * @param head
     * @return
     */
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode prev = new ListNode(-1);
        prev.next = head;
        ListNode cur = prev;
        ListNode runner = prev;
        // 2 -> 1
        while (runner != null && runner.next != null) {
            cur = cur.next;
            runner = runner.next.next;
        }
        // split as two parts left and right
        ListNode secondHalf = cur.next;
        cur.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(secondHalf);
        // merge
        prev = new ListNode(-1);
        cur = prev;
        while (left != null && right != null) {
            if (left.val <= right.val) {
                cur.next = left;
                left = left.next;
            } else {
                cur.next = right;
                right = right.next;
            }
            cur = cur.next;
        }
        while (left != null) {
            cur.next = left;
            left = left.next;
            cur = cur.next;
        }
        while (right != null) {
            cur.next = right;
            right = right.next;
            cur = cur.next;
        }
        return prev.next;
    }
    /**
     * this is to implement quick sort
     * @param head
     * @return
     */
    public ListNode sortListI(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        /*
         * check if the list already sorted
         * this step is not necessary in reality but let it pass
         * leetcode
         */
        ListNode cur = head;
        ListNode next = cur.next;
        boolean needSort = false;
        while (next != null) {
            if (cur.val > next.val) {
                needSort = true;
                break;
            }
            cur = cur.next;
            next = next.next;
        }
        if (!needSort) {
            return head;
        }
        // partition
        Pair<ListNode, ListNode> nodePair = partition(head);
        // sort left
        ListNode node1 = sortListI(nodePair.getKey());
        // sort right
        ListNode node2 = sortListI(nodePair.getValue());
        if (node1 != null) {
            // head is always the end of first part
            head.next = node2;
            return node1;
        }
        return node2;
    }

    /**
     * split the first part into two parts
     * @param head
     * @return
     */
    private Pair<ListNode, ListNode> partition(ListNode head) {
        if (head == null) {
            return new Pair<>(null, null);
        }
        ListNode node1 = new ListNode(-1);
        ListNode node2 = new ListNode(-1);
        ListNode cur1 = node1;
        ListNode cur2 = node2;
        ListNode pivot = head;
        head = head.next;
        pivot.next = null;
        while (head != null) {
            if (head.val < pivot.val) {
                cur1.next = head;
                cur1 = cur1.next;
            } else {
                cur2.next = head;
                cur2 = cur2.next;
            }
            head = head.next;
            cur1.next = null;
            cur2.next = null;
        }
        cur1.next = pivot;
        return new Pair<>(node1.next, node2.next);
    }

    public static void main(String[] args) {
        SortList sortList = new SortList();
        ListNode node1 = new ListNode(4);
        ListNode node2 = new ListNode(9);
        ListNode node3 = new ListNode(14);
        ListNode node4 = new ListNode(5);
        ListNode node5 = new ListNode(-3);
        ListNode node6 = new ListNode(1);
        ListNode node7 = new ListNode(8);
        ListNode node8 = new ListNode(5);
        ListNode node9 = new ListNode(11);
        ListNode node10 = new ListNode(15);
        node1.next = node2;
//        node2.next = node3;
//        node3.next = node4;
//        node4.next = node5;
//        node5.next = node6;
//        node6.next = node7;
//        node7.next = node8;
//        node8.next = node9;
//        node9.next = node10;
        ListNode node = sortList.sortList(node1);
        System.out.println();
    }

}
