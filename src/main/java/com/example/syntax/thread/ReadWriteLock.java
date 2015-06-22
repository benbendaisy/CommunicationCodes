package com.example.syntax.thread;

/**
 * Created by benbendaisy on 6/15/15.
 */
public class ReadWriteLock {
    private int readers = 0;
    private int writers = 0;
    private int writerRequests = 0;

    public synchronized void lockRead() throws InterruptedException {
        while (writers > 0 || writerRequests > 0) {
            wait();
        }
        readers++;
    }

    public synchronized void unlockRead() {
        readers--;
        notifyAll();
    }

    public synchronized void lockWrite() throws InterruptedException {
        writerRequests++;
        while (readers > 0 || writers > 0) {
            wait();
        }
        writerRequests--;
        writers++;
    }

    public synchronized void unlockWrite() throws InterruptedException {
        writers--;
        notifyAll();
    }
}
