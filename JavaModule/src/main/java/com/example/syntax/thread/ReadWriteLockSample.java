package com.example.syntax.thread;

import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

/**
 * Created by benbendaisy on 6/15/15.
 */
public class ReadWriteLockSample {
    ReadWriteLock readWriteLock = new ReentrantReadWriteLock();

    public void read() {
        readWriteLock.readLock().lock();
        try {
            System.out.println("in reading");
        } finally {
            readWriteLock.readLock().unlock();
        }
    }

    public void write() {
        readWriteLock.writeLock().lock();
        try {
            System.out.println("in writing");
        } finally {
            readWriteLock.writeLock().unlock();
        }
    }
}
