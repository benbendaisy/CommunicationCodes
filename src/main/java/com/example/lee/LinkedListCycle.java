package com.example.lee;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 12/22/14.
 * Given a linked list, determine if it has a cycle in it.
 * Follow up:
 * Can you solve it without using extra space?
 */
public class LinkedListCycle {

    //with extra space
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        Set<ListNode> set = new HashSet<ListNode>();
        while(head != null){
            if(!set.add(head)){
                return true;
            }
            head = head.next;
        }
        return false;
    }


    //without extra space
    public boolean hasCycle1(ListNode head) {
        if(head == null){
            return false;
        }
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow){
                return true;
            }
        }
        return false;
    }
}
