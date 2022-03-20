package com.example.lee.firstRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 12/22/14.
 * Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
 * get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
 * set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
 */
class ListNode{
    int value;
    int key;
    ListNode next;
    ListNode prev;
    ListNode(int key, int value){
        this.value = value;
        this.key = key;
        this.next = null;
        this.prev = null;
    }

    //both hashCode and equals are not necessarily needed in this program
    @Override
    public int hashCode(){
        final int prime = 31;
        int result = 1;
        result = prime * result + this.value;
        result = prime * result + (this.prev == null ? 0 : this.prev.hashCode());
        result = prime * result + (this.next == null ? 0 : this.next.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }
        if (!(o instanceof ListNode)) {
            return false;
        }
        ListNode c = (ListNode) o;
        return Integer.compare(this.value, c.value) == 0;
    }

}
public class LRUCache {
    int capacity;
    int current;
    ListNode head;
    ListNode tail;
    Map<Integer, ListNode> map = new HashMap<Integer, ListNode>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.current = 0;
    }

    public int get(int key) {
        if(this.map.containsKey(key)){
            int val = this.map.get(key).value;
            set(key, val);
            return val;

        }
        return -1;
    }

    public void removeKey(int key){
        if(!this.map.containsKey(key)){
            return;
        }
        ListNode currentNode = this.map.get(key);
        if(this.head == currentNode){
            if(this.head.next != null){
                this.head = this.head.next;
                this.head.prev = null;
                if(this.head.next != null){
                    this.head.next.prev = this.head;
                }
            } else {
                this.tail = this.head = null;
            }
        } else if(this.tail == currentNode){
            if(this.tail.prev != null){
                this.tail = this.tail.prev;
                this.tail.next = null;
            } else {
                this.tail = this.head = null;
            }
        } else {
            currentNode.prev.next = currentNode.next;
            currentNode.next.prev = currentNode.prev;
        }
        this.current--;
        this.map.remove(key);
    }

    public void set(int key, int value) {
        removeKey(key);
        ListNode node = new ListNode(key, value);
        this.map.put(key, node);
        if(this.head == null){
            this.head = this.tail = node;
            this.current = 1;
            return;
        }
        this.tail.next = node;
        node.prev = this.tail;
        this.tail = node;
        this.current++;
        if(this.current > this.capacity){
            if(this.head.next == null){
                this.tail = this.head = null;
            } else {
                this.map.remove(this.head.key);
                this.head = this.head.next;
                this.head.prev = null;
            }
            this.current--;
        }
    }
    public static void main(String[] args) {

        LRUCache cache = new LRUCache(1);
        cache.set(2, 1);
        System.out.println(cache.get(2));
        cache.set(3, 2);
        System.out.println(cache.get(2));
        System.out.println(cache.get(3));
    }
}