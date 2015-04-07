package com.example.lee.secondRound;

import com.example.lee.model.RandomListNode;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/3/15.
 */
public class CopyListwithRandomPointer {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (null == head) return head;
        RandomListNode dummyHead = new RandomListNode(0);
        dummyHead.next = head;
        Map<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        while (null != head) {
            RandomListNode node = null;
            if (!map.containsKey(head)) {
                node = new RandomListNode(head.label);
                map.put(head, node);
            } else {
                node = map.get(head);
            }
            RandomListNode t = head.next;
            head.next = node;
            node.next = t;
            //node.random = head.random;

            RandomListNode random = null;
            if (null != head.random) {
                if (!map.containsKey(head.random)) {
                    random = new RandomListNode(head.random.label);
                    map.put(head.random, random);
                } else {
                    random = map.get(head.random);
                }
                node.random = random;
            }
            head = head.next.next;
        }

        head = dummyHead.next;
        RandomListNode newHead = dummyHead;
        while (null != head) {
            RandomListNode next = head.next;
            head.next = next.next;
            newHead.next = next;
            head = head.next;
            newHead = newHead.next;
        }
        return dummyHead.next;
    }

    public RandomListNode copyRandomListI(RandomListNode head) {
        if (null == head) return head;
        RandomListNode dummyHead = new RandomListNode(0);
        dummyHead.next = head;
        while (null != head) {
            RandomListNode node = new RandomListNode(head.label);
            node.next = head.next;
            head.next = node;
            node.random = head.random;
            head = node.next;
        }
        //need to consider the last node if its random points to original node
//        RandomListNode newHead = dummyHead.next.next;
//        while (null != newHead && null != newHead.next) {
//            if (null != newHead.random) newHead.random = newHead.random.next;
//            newHead = newHead.next.next;
//        }
//        if (null != newHead.random) newHead.random = newHead.random.next;
        head = dummyHead.next;
        while(head != null && head.next != null){
            if(head.next.random != null){
                head.next.random = head.next.random.next;
            }
            head = head.next.next;
        }
        head = dummyHead.next;
        RandomListNode newHead = dummyHead;
        while (null != head) {
            RandomListNode next = head.next;
            head.next = next.next;
            newHead.next = next;
            head = head.next;
            newHead = newHead.next;
        }
        return dummyHead.next;
    }

    public static void main(String[] args) {
        CopyListwithRandomPointer copyListwithRandomPointer = new CopyListwithRandomPointer();
        RandomListNode node = new RandomListNode(-1);
        RandomListNode node1 = new RandomListNode(-1);
        node.next = node1;
        node.random = node1;
        copyListwithRandomPointer.copyRandomListI(node);
    }
}
