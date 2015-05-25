package com.example.syntax;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by pzhong1 on 5/15/15.
 */
public class GenericExample <T> {
    List<? super T> list = new ArrayList<>();
    Object[] objects;
    int start = 0;
    int end = 0;
    int length = 0;
    int capacity = 0;
    public GenericExample(int capacity) {
        objects = new Object[capacity];
        this.capacity = capacity;
    }

    public boolean offer(T obj) {
        if (length == capacity) return false;
        if (end == objects.length) end = 0;
        objects[end] = obj;
        length++;
        end++;
        list.add(obj);
        return true;
    }

    public T poll() {
        if (length == 0) return null;
        if (start == objects.length) start = 0;
        T t = (T) objects[start];
        length--;
        start++;
        return t;
    }

    public T peer() {
        if (length == 0) return null;
        if (start == objects.length) start = 0;
        return (T) objects[start];
    }

    public boolean isEmpty() {
        return length == 0 ? true : false;
    }

    public static void main(String[] args) {
        GenericExample<String> stringGenericExample = new GenericExample<String>(2);
        System.out.println(stringGenericExample.offer("abc"));
        System.out.println(stringGenericExample.offer("def"));
        System.out.println(stringGenericExample.offer("hij"));
        System.out.println(stringGenericExample.peer());
        System.out.println(stringGenericExample.poll());
        System.out.println(stringGenericExample.poll());
        System.out.println(stringGenericExample.poll());
        System.out.println(stringGenericExample.offer("abc"));
        System.out.println(stringGenericExample.offer("def"));
        System.out.println(stringGenericExample.offer("hij"));
        System.out.println(stringGenericExample.peer());
        System.out.println(stringGenericExample.poll());
        System.out.println(stringGenericExample.poll());
        System.out.println(stringGenericExample.poll());
        System.out.println(stringGenericExample.list);

    }
}
