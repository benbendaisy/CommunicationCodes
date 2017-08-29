package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class LRUCache {
    private static class Node {
        Node prev;
        Node next;
        int val;
        int key;
    }
    private Map<Node, Integer> _nodeIntegerMap = new HashMap<>();
    private Map<Integer, Node> _cache = new HashMap<>();
    private int _capacity = 0;
    private int _currentSize = 0;
    private Node _head;
    private Node _tail;
    public LRUCache(int capacity) {
        _capacity = capacity;
    }

    public int get(int key) {
        if (!_cache.containsKey(key)) {
            return -1;
        }
        Node retrieved = _cache.get(key);
        put(key, retrieved.val);
        return retrieved.val;
    }

    private void remove(int key) {
        if (!_cache.containsKey(key)) {
            return;
        }
        Node retrieved = _cache.get(key);
        _cache.remove(key);
        _nodeIntegerMap.remove(retrieved);
        _currentSize--;
        if (retrieved == _tail) {
            if (_tail.prev != null) {
                _tail = _tail.prev;
                _tail.next = null;
            } else {
                _head = _tail = null;
            }
        } else {
            if (retrieved == _head) {
                if (_head.next !=  null) {
                    _head = _head.next;
                    _head.prev = null;
                    if (_head.next != null) {
                        _head.next.prev = _head;
                    }
                } else {
                    _head = _tail = null;
                }
            } else {
                if (retrieved.prev != null) {
                    retrieved.prev.next = retrieved.next;
                }
                if (retrieved.next != null) {
                    retrieved.next.prev = retrieved.prev;
                }
            }
        }
    }

    private void insert(int key, int value) {
        Node node = new Node();
        node.key = key;
        node.val = value;
        _cache.put(key, node);
        _nodeIntegerMap.put(node, key);
        _currentSize++;
        if (_tail == null) {
            _head = _tail = node;
        } else {
            _tail.next = node;
            node.prev = _tail;
            _tail = node;
        }
        if (_currentSize > _capacity) {
            remove(_head.key);
        }
    }

    public void put(int key, int value) {
        remove(key);
        insert(key, value);
    }
}
