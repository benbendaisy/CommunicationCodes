package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 7/1/17.
 */
public class ReverseNodesInKGroup {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k < 2) {
            return head;
        }
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode prev = dummyHead;
        ListNode cur = head;
        int idx = 0;
        while (cur != null) {
            idx++;
            if (idx % k == 0) {
                prev = reverseNodesInKGroup(prev, cur.next);
                cur = prev.next;
            } else {
                cur = cur.next;
            }
        }
        return dummyHead.next;
    }

    /**
     * 1 -> 2 -> 3
     * 1 -> 2 -> 3
     * 0 -> 1 -> 2 -> 3
     * @param startNode
     * @param endNode
     * @return
     */
    private ListNode reverseNodesInKGroup(ListNode startNode, ListNode endNode) {
        ListNode last = startNode.next; // 1
        ListNode cur = last.next; // 2
        while (cur != endNode) {
            last.next = cur.next; //
            cur.next = startNode.next;
            startNode.next = cur;
            cur = last.next;
        }
        return last;
    }


    private ListNode reverseNodesInKGroups(ListNode prev, ListNode end) {
        ListNode last = prev.next;
        ListNode cur = last.next;
        while (cur != end) {
            last.next = cur.next;
            cur.next = prev.next;
            prev.next = cur;
            cur = last.next;
        }
        return last;
    }
}
