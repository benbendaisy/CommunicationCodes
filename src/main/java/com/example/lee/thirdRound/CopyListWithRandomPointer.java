package com.example.lee.thirdRound;

import com.example.lee.model.RandomListNode;

public class CopyListWithRandomPointer {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }
        RandomListNode cur = head;
        // duplicate nodes
        while (cur != null) {
            RandomListNode newNode = new RandomListNode(cur.label);
            newNode.next = cur.next;
            cur.next = newNode;
            newNode.random = cur.random;
            cur = newNode.next;
        }
        cur = head;
        int cnt = 0;
        // make the random pointer to point the right node
        while (cur != null) {
            cnt++;
            if (cnt%2 == 0 && cur.random != null) {
                cur.random = cur.random.next;
            }
            cur = cur.next;
        }
        RandomListNode dummyHead = new RandomListNode(-1);
        dummyHead.next = head.next;
        RandomListNode newCur = dummyHead;
        cur = head;
        // break the chain
        while (cur != null) {
            newCur.next = cur.next;
            newCur = newCur.next;
            if (newCur != null) {
                cur.next = newCur.next;
            }
            cur = cur.next;
        }
        return dummyHead.next;
    }
}
