package com.example.lee.secondRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 3/26/15.
 */
public class LRUCache {
    private class DoubleLinkList {
        public int key;
        public int value;
        public DoubleLinkList prev;
        public DoubleLinkList next;
        public DoubleLinkList(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    DoubleLinkList head;
    DoubleLinkList tail;

    private int capacity;
    Map<Integer, DoubleLinkList> map;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<Integer, DoubleLinkList>();
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            int value = map.get(key).value;
            deleteNode(key);
            insert(key, value);
            return value;
        } else {
            return -1;
        }
    }

    public void set(int key, int value) {
        deleteNode(key);
        if (map.size() == this.capacity) {
            deleteNode(head.key);
        }
        insert(key, value);
    }

    public void insert(int key, int value) {
        if (null == head) {
            head = new DoubleLinkList(key, value);
            tail = head;
            map.put(key, head);
            return;
        }
        DoubleLinkList t = new DoubleLinkList(key, value);
        map.put(key, t);
        tail.next = t;
        t.prev = tail;
        tail = t;
    }

    public void deleteNode(int key) {
        if (map.containsKey(key)) {
            DoubleLinkList node = map.get(key);
            map.remove(key);
            if (node.prev != null) node.prev.next = node.next;
            if (node.next != null) node.next.prev = node.prev;
            if (tail == node) tail = node.prev;
            if (head == node) head = node.next;
        }
    }

    public static void main(String[] args) {
        LRUCache lruCache = new LRUCache(2);
        lruCache.set(2, 1);
        lruCache.set(1, 1);
        System.out.println(lruCache.get(2));
        lruCache.set(4, 1);
        System.out.println(lruCache.get(1));
        System.out.println(lruCache.get(2));
    }
}
