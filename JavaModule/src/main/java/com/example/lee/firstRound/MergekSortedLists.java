package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;
import com.example.lee.model.ListNode;

/**
 * Created by benbendaisy on 2/26/15.
 */
public class MergekSortedLists {
    public ListNode mergeKLists(List<ListNode> lists) {
        if (null == lists || lists.size() == 0) {
            return null;
        }
        while (lists.size() > 1) {
            ListIterator<ListNode> listIterator = lists.listIterator();
            while (listIterator.hasNext()) {
                ListNode node1 = null;
                ListNode node2 = null;
                node1 = listIterator.next();
                if (listIterator.hasNext()) {
                    listIterator.remove();
                    node2 = listIterator.next();
                    listIterator.remove();
                } else {
                    continue;
                }
                ListNode listNode = mergeLists(node1, node2);
                if (null != listNode) {
                    listIterator.add(listNode);
                }
            }
        }
        if (lists.isEmpty()) {
            return null;
        }
        return lists.get(0);
    }

    private ListNode mergeLists(ListNode node1, ListNode node2) {
        if (null == node1) {
            return node2;
        } else if (null == node2) {
            return node1;
        }
        ListNode prev = new ListNode(0);
        if (node1.val < node2.val) {
            prev.next = node1;
            node1 = node1.next;
        } else {
            prev.next = node2;
            node2 = node2.next;
        }
        ListNode cur = prev.next;
        while (node1 != null && node2 != null) {
            if (node1.val < node2.val) {
                cur.next = node1;
                node1 = node1.next;
            } else {
                cur.next = node2;
                node2 = node2.next;
            }
            cur = cur.next;
        }
        while (null != node1) {
            cur.next = node1;
            node1 = node1.next;
            cur = cur.next;
        }
        while (null != node2) {
            cur.next = node2;
            node2 = node2.next;
            cur = cur.next;
        }
        return prev.next;
    }

    public static void main(String[] args) {
        MergekSortedLists mergekSortedLists = new MergekSortedLists();
        List<ListNode> lists = new ArrayList<ListNode>();
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(-1);
        lists.add(node1);
        lists.add(null);
        lists.add(node2);
        mergekSortedLists.mergeKLists(lists);
    }

}
