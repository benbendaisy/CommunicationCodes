package com.example.ip.vmware;

/**
 * Created by pzhong1 on 6/15/15.
 *
 * http://www.tutorialspoint.com/java/java_thread_deadlock.htm
 *
 * idea is trying to create deadlock and how to solve it
 *
 */
public class DeadLock {
    public static final Object lock1 = new Object();
    public static final Object lock2 = new Object();

    private static class ThreadDemo1 implements Runnable {
        @Override
        public void run() {
            synchronized (lock1) {
                System.out.println("Thread 1: Holding lock 1...");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread 1: Waiting for lock 2...");
                synchronized (lock2) {
                    System.out.println("Thread 1: Holding lock 1 & 2...");
                }
            }
        }
    }

    private static class ThreadDemo2 extends Thread {
        @Override
        public void run() {
            synchronized (lock2) {
                System.out.println("Thread 2: Holding lock 2...");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread 2: Waiting for lock 1...");
                synchronized (lock1) {
                    System.out.println("Thread 2: Holding lock 1 & 2...");
                }
            }
        }
    }

    private static class ThreadDemo3 implements Runnable {
        @Override
        public void run() {
            synchronized (lock1) {
                System.out.println("Thread 3: Holding lock 1...");
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread 3: Waiting for lock 2...");
                synchronized (lock2) {
                    System.out.println("Thread 3: Holding lock 1 & 2...");
                }
            }
        }
    }

    private static class ThreadDemo4 extends Thread {
        @Override
        public void run() {
            synchronized (lock1) {
                System.out.println("Thread 4: Holding lock 1...");
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread 4: Waiting for lock 2...");
                synchronized (lock2) {
                    System.out.println("Thread 4: Holding lock 1 & 2...");
                }
            }
        }
    }

    public static void main(String args[]) {
        ThreadDemo1 t1 = new ThreadDemo1();
        ThreadDemo2 t2 = new ThreadDemo2();
        ThreadDemo3 t3 = new ThreadDemo3();
        ThreadDemo4 t4 = new ThreadDemo4();
        Thread t5 = new Thread(t1);
        t5.start();
        t2.start();
    }
}
