package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 3/28/15.
 */
public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        if (null == head || null == head.next) return false;
        ListNode runner = head.next;
        while (null != runner && null != runner.next && runner != head) {
            head = head.next;
            runner = runner.next.next;
        }
        return runner == head ? true : false;
    }

    public boolean hasCycleI(ListNode head) {
        if (null == head || null == head.next) return false;
        Set<ListNode> visited = new HashSet<ListNode>();
        while (null != head) {
            head = head.next;
            if (!visited.add(head)) return true;
        }
        return false;
    }
}
