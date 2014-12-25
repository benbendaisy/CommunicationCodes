package com.example.lee;

import com.example.lee.model.RandomListNode;

/**
 * A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
 * Return a deep copy of the list.
 * Created by benbendaisy on 12/23/14.
 */
public class CopyListwithRandomPointer {
    public RandomListNode copyRandomList(RandomListNode head) {
        if(head == null){
            return null;
        }

        RandomListNode prev = new RandomListNode(0);
        prev.next = head;
        //duplicate each node
        while(head != null){
            RandomListNode head1 = new RandomListNode(head.label);
            head1.random = head.random;
            head1.next = head.next;
            head.next = head1;
            head = head1.next;
        }

        head = prev.next;
        //make the random node point its next
        while(head != null && head.next != null){
            if(head.next.random != null){
                head.next.random = head.next.random.next;
            }
            head = head.next.next;
        }

        head = prev.next;
        prev.next = head.next;
        //split list into two
        while(head != null && head.next != null && head.next.next != null){
            RandomListNode tempNode = head.next;
            head.next = head.next.next;
            head = head.next;
            tempNode.next = head.next;
        }
        head.next = null;
        return prev.next;
    }

    public static void main(String[] args) {
        RandomListNode randomListNode = new RandomListNode(-1);
        randomListNode.next = null;
        CopyListwithRandomPointer copyListwithRandomPointer = new CopyListwithRandomPointer();
        RandomListNode head = copyListwithRandomPointer.copyRandomList(randomListNode);
        System.out.println(head.label);
    }
}
