package com.example.designPattern.objectPool;

import java.util.Enumeration;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Created by benbendaisy on 6/8/15.
 *
 * refer to https://sourcemaking.com/design_patterns/object_pool
 */
public abstract class ObjectDesignPool<T> {
    private long expirationTime;
    private ConcurrentHashMap<T, Long> locked, unlocked;

    public ObjectDesignPool() {
        expirationTime = 30000;
        locked = new ConcurrentHashMap<>();
        unlocked = new ConcurrentHashMap<>();
    }

    protected abstract T create();

    public abstract boolean validate(T o);

    public abstract void expire(T o);

    public synchronized T checkOut() {
        long now = System.currentTimeMillis();
        T t;
        if (unlocked.size() > 0) {
            Enumeration<T> e = unlocked.keys();
            while (e.hasMoreElements()) {
                t = e.nextElement();
                if ((now - unlocked.get(t)) > expirationTime) {
                    unlocked.remove(t);
                    expire(t);
                    t = null;
                } else {
                    if (validate(t)) {
                        unlocked.remove(t);
                        locked.put(t, now);
                        return t;
                    } else {
                        unlocked.remove(t);
                        expire(t);
                        t = null;
                    }
                }
            }
        }
        t = create();
        locked.put(t, now);
        return t;
    }

    public synchronized void checkIn(T t) {
        locked.remove(t);
        unlocked.put(t, System.currentTimeMillis());
    }
}
