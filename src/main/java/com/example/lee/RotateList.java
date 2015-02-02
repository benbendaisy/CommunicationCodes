package com.example.lee;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 1/23/15.
 *
 * Given a list, rotate the list to the right by k places, where k is non-negative.
 *
 * For example:
 * Given 1->2->3->4->5->NULL and k = 2,
 * return 4->5->1->2->3->NULL.
 */
public class RotateList {
    public ListNode rotateRight(ListNode head, int n) {
        if(head == null || n == 0){
            return head;
        }

        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode current = head;
        int count = 0;
        while(current != null){
            count++;
            prev = current;
            current = current.next;
        }

        if(count == 1){
            return head;
        }

        int move = count - (n % count);

        if(move <= 0 || move == count){
            return head;
        }

        ListNode prev1 = new ListNode(0);
        prev1.next = head;
        current = head;

        //get the new head
        while(move > 0 && current != null){
            prev1 = current;
            current = current.next;
            move--;
        }

        //disconnect the end
        prev1.next = null;

        //connect the rest to head
        prev.next = head;

        //return the new head
        return current;
    }
}
