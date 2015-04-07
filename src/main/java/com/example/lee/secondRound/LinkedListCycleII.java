package com.example.lee.secondRound;

import com.example.lee.model.ListNode;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by benbendaisy on 3/30/15.
 */
public class LinkedListCycleII {
    //refer http://www.cnblogs.com/hiddenfox/p/3408931.html for illustration
    //key point to prove 2 * (a + b) = a + b + c + b => a = c
    public ListNode detectCycle(ListNode head) {
        if (null == head || null == head.next) return null;
        ListNode cur = head.next, runner = head.next.next;
        while (null != runner && null != runner.next & cur != runner) {
            cur = cur.next;
            runner = runner.next.next;
        }
        if (cur == runner) {
            cur = head;
            while (runner != cur) {
                cur = cur.next;
                runner = runner.next;
            }
            return cur;
        }
        return null;
    }

    public ListNode detectCycleI(ListNode head) {
        if (null == head || null == head.next) return null;
        Set<ListNode> set = new HashSet<ListNode>();
        while (null != head && set.add(head)) {
            head = head.next;
        }
        return head;
    }

}
