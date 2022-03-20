package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

import java.util.List;

public class ReverseLinkedListII {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null || m == n) {
            return head;
        }

        ListNode dummyHead = new ListNode(-1);
        dummyHead.next = head;
        ListNode start = null;
        ListNode cur = dummyHead;
        int idx = 0;
        while (idx <= n && cur != null) {
            if (idx == m - 1) {
                start = cur;
            }
            idx++;
            cur = cur.next;
        }
        groupReverse(start, cur);
        return dummyHead.next;
    }

    private void groupReverse(ListNode start, ListNode end) {
        ListNode last = start.next;
        ListNode cur = last.next;
        while (cur != end) {
            last.next = cur.next;
            cur.next = start.next;
            start.next = cur;
            cur = last.next;
        }
    }

    public static void main(String[] args) {
        ReverseLinkedListII reverseLinkedListII = new ReverseLinkedListII();
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        node1.next = node2;
        node2.next = node3;
        reverseLinkedListII.reverseBetween(node1, 1, 3);
    }
}
