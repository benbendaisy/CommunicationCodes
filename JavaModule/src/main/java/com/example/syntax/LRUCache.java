package com.example.syntax;

import java.util.LinkedHashMap;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentLinkedQueue;

/**
 * Created by benbendaisy on 5/29/15.
 */
public class LRUCache<Key, Value> {
    private ConcurrentHashMap<Key, Value> map;
    private ConcurrentLinkedQueue<Key> queue;
    private int capacity = 0;
    public LRUCache(int capacity){
        this.capacity = capacity;
        map = new ConcurrentHashMap<Key, Value>(capacity);
        queue = new ConcurrentLinkedQueue<Key>();
    }

    public void remove (Key key) {
        if (map.containsKey(key)) {
            map.remove(key);
            queue.remove(key);
        }
    }

    public Value get(Key key) {
        Value v = null;
        if (map.containsKey(key)) {
            v = map.get(key);
            queue.remove(key);
            queue.add(key);
        }
        return v;
    }

    public void insert(Key key, Value value) {
        if (map.size() == capacity) {
            Key tKey = queue.poll();
            map.remove(tKey);
        }
        map.put(key, value);
        queue.add(key);
    }
}
