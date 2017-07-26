package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

import java.util.List;

/**
 * Created by benbendaisy on 7/16/17.
 */
public class RemoveDuplicatesFromSortedListII {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummyHead = new ListNode(0);
        ListNode cur = head;
        ListNode end = dummyHead;
        while (cur != null) {
            if (cur.next != null && cur.val == cur.next.val) {
                while (cur.next != null && cur.val == cur.next.val) {
                    cur = cur.next;
                }
            } else {
                end.next = cur;
                end = end.next;
            }
            cur = cur.next;
        }
        end.next = null;
        return dummyHead.next;
    }

    public static void main(String[] args) {
        RemoveDuplicatesFromSortedListII removeDuplicatesFromSortedListII = new RemoveDuplicatesFromSortedListII();
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(2);
        node1.next = node2;
        removeDuplicatesFromSortedListII.deleteDuplicates(node1);
    }
}
