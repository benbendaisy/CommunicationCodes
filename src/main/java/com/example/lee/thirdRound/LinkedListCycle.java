package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        ListNode cur = head;
        ListNode runner = head;
        while (runner != null && runner.next != null) {
            cur = cur.next;
            runner = runner.next.next;
            if (cur == runner) {
                return true;
            }
        }
        return false;
    }
}
