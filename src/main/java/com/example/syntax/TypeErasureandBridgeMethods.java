package com.example.syntax;

import java.util.ArrayList;

/**
 * Created by pzhong1 on 4/29/15.
 *
 * refer to https://docs.oracle.com/javase/tutorial/java/generics/bridgeMethods.html
 */
public class TypeErasureandBridgeMethods {
    public class Node<T> {

        public T data;

        public Node(T data) { this.data = data; }

        public void setData(T data) {
            System.out.println("Node.setData");
            this.data = data;
        }
    }

    public class MyNode extends Node<Integer> {
        public MyNode(Integer data) { super(data); }

        public void setData(Integer data) {
            System.out.println("MyNode.setData");
            super.setData(data);
        }
    }

    //refer to http://www.programcreek.com/2011/12/java-type-erasure-mechanism-example/
    //use ? instead Object
    public static void main(String args[]) {
        ArrayList<Object> al = new ArrayList<Object>();
        al.add("abc");
        test(al);
        Integer[] array = {1, 2, 3, 4, 2, 3};
        System.out.println(count(array, 2));
    }

    public static void test(ArrayList<?> al){
        for(Object e: al){//no matter what type, it will be Object
            System.out.println(e);
// in this method, because we don't know what type ? is, we can not add anything to al.
        }
    }

    public static <T extends Integer> int count(T[] anArray, T elem) {
        int cnt = 0;
        for (T e : anArray)
            if (e.equals(elem))
                ++cnt;
        return cnt;
    }
}
