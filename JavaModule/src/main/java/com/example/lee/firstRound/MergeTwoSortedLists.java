package com.example.lee.firstRound;

import com.example.lee.model.ListNode;
/**
 * Created by benbendaisy on 1/19/15.
 *
 * Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
 */
public class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        } else if(l2 == null){
            return l1;
        }
        ListNode pre = new ListNode(0);
        ListNode current = pre;
        while(l1 != null && l2 != null){
            if(l1.val < l2.val){
                current.next = l1;
                current = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                current = l2;
                l2 = l2.next;
            }
        }

        while(l1 != null){
            current.next = l1;
            current = l1;
            l1 = l1.next;
        }

        while(l2 != null){
            current.next = l2;
            current = l2;
            l2 = l2.next;
        }

        return pre.next;
    }
}
