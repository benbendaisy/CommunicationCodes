package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

import java.util.HashSet;
import java.util.Set;

public class LinkedListCycleII {
    public ListNode detectCycle(ListNode head) {
        ListNode cur = head;
        ListNode runner = head;
        while (runner != null && runner.next != null) {
            cur = cur.next;
            runner = runner.next.next;
            if (runner == cur) {
                break;
            }
        }

        // no cycle
        if (runner != cur) {
            return null;
        }

        // there is a cycle
        cur = head;
        while (cur != runner) {
            cur = cur.next;
            runner = runner.next;
        }
        return cur;
    }
    /**
     * passed leetcode but with o(n) space complexity
     * @param head
     * @return
     */
    public ListNode detectCycleI(ListNode head) {
        ListNode cur = head;
        Set<ListNode> set = new HashSet<>();
        while (cur != null) {
            if (!set.add(cur)) {
                return cur;
            }
            cur = cur.next;
        }
        return cur;
    }
}
