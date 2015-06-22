package com.example.ip.frommitbbs;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Created by benbendaisy on 6/15/15.
 *
 * refer to http://www.mitbbs.com/article_t/JobHunting/32988733.html
 *
 */
public class CacheLoading<K, V> {
    private Map<K, V> cache = new HashMap<>();
    private ConcurrentHashMap<K, ReentrantLock> keyLock = new ConcurrentHashMap<>();

    public V get(K key) {
        ReentrantLock lock = new ReentrantLock();
        lock = keyLock.putIfAbsent(key, lock);
        lock.lock();
        V value = null;
        try {
            if (cache.containsKey(key)) {
                value = cache.get(key);
            } else {
                value = loadValueWithKey(key);
                cache.put(key, value);
            }
        } finally {
            lock.unlock();
        }
        return value;
    }
    private V loadValueWithKey(K key) {
        return null;
    }
}
