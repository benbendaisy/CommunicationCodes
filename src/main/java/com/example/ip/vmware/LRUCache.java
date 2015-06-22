package com.example.ip.vmware;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by pzhong1 on 6/14/15.
 *
 * uber also asks the same question
 *
 */
public class LRUCache<K, V> {
    private static class DoubleLinkNode<K, V> {
        K key;
        V value;
        DoubleLinkNode next;
        DoubleLinkNode prev;
        public DoubleLinkNode(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private DoubleLinkNode head = new DoubleLinkNode(null, null);
    private DoubleLinkNode end = new DoubleLinkNode(null, null);
    private Map<K, DoubleLinkNode> map;
    private final int limit;
    public LRUCache(int limit) {
        this.limit = limit;
        map = new HashMap<K, DoubleLinkNode>();
        head.next = end;
        end.prev = head;
    }

    public void remove(K key) {
        if (!map.containsKey(key)) return;
        DoubleLinkNode node = map.get(key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
        map.remove(key);
    }

    public void set(K key, V value) {
        if (map.containsKey(key)) {
            remove(key);
        } else if (map.size() == limit) {
            remove((K) head.next.key);
        }
        DoubleLinkNode node = new DoubleLinkNode(key, value);
        node.prev = end.prev;
        node.next = end;
        end.prev.next = node;
        end.prev = node;
        map.put(key, node);
    }

    public V get(K key) {
        if (!map.containsKey(key)) return null;
        DoubleLinkNode node = map.get(key);
        V value = (V) node.value;
        set(key, value);
        return value;
    }

}
