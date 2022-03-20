package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;
import javafx.util.Pair;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class MergeKSortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        } else if (lists.length == 1) {
            return lists[0];
        }
        Comparator<ListNode> comparator = (a, b) -> Integer.compare(a.val, b.val);
        Queue<ListNode> pq = new PriorityQueue<>(comparator);
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                pq.add(lists[i]);
            }
        }
        ListNode prev = new ListNode(0);
        ListNode cur = prev;
        while (!pq.isEmpty()) {
            ListNode topNode = pq.poll();
            cur.next = topNode;
            cur = cur.next;
            if (topNode.next != null) {
                pq.add(topNode.next);
            }
        }
        return prev.next;
    }
}
