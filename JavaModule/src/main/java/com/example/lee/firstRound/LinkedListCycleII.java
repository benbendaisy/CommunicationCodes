package com.example.lee.firstRound;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 12/22/14.
 * Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
 * Follow up:
 * Can you solve it without using extra space?
 */
public class LinkedListCycleII {
    //with extra space
    public ListNode detectCycle(ListNode head) {
        if(head == null){
            return head;
        }
        Set<ListNode> set = new HashSet<ListNode>();
        while(head != null && set.add(head)){
            head = head.next;
        }
        return head;
    }


    //without extra space. illustration is shown http://blog.sina.com.cn/s/blog_6a0e04380101a9o2.html
    public ListNode detectCycle1(ListNode head) {
        if(head == null){
            return head;
        }
        ListNode slow = head;
        ListNode fast = head;
        boolean hasCycle = false;
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow){
                hasCycle = true;
                break;
            }
        }
        if(hasCycle){
            slow = head;
            while(fast != null){
                if(fast == slow){
                    return fast;
                }
                fast = fast.next;
                slow = slow.next;
            }
        }
        return null;
    }

}
