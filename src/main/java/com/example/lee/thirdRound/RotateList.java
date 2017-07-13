package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 7/11/17.
 */
public class RotateList {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k < 1) {
            return head;
        }

        long count = 0;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode cur = head;
        ListNode end = dummyHead;
        while (cur != null) {
            count++;
            cur = cur.next;
            end = end.next;
        }

        long steps = count - k % count;
        cur = head;
        ListNode prev = dummyHead;
        if (steps == count) {
            return dummyHead.next;
        }
        while (steps > 0) {
            cur = cur.next;
            prev = prev.next;
            steps--;
        }

        dummyHead.next = cur;
        prev.next = null;
        end.next = head;
        return dummyHead.next;
    }

    public static void main(String[] args) {
        RotateList rotateList = new RotateList();
        ListNode node1 = new ListNode(0);
        ListNode node2 = new ListNode(1);
        node1.next = node2;
        node2.next = null;
        // 0 -> 1    1
        rotateList.printListNodes(node1);
        ListNode node = rotateList.rotateRight(node1, 3);
        rotateList.printListNodes(node);
    }

    private void printListNodes(ListNode node) {
        while (node != null) {
            System.out.print(node.val);
            System.out.print("->");
            node = node.next;
        }
        System.out.print("null\n");
    }
}
