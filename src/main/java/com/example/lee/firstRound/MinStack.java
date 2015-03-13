package com.example.lee.firstRound;

/**
 * Created by pzhong1 on 12/26/14.
 */
public class MinStack {
    private Element head;
    public void push(int x) {
        if(head == null){
            head = new Element(x, Integer.MIN_VALUE);
        } else {
            int min = head.getMinValue() < x ? head.getMinValue() : x;
            Element current = new Element(x, min);
            current.next = head;
            head = current;
        }
    }

    public void pop() {
        if(head != null){
            head = head.next;
        }
    }

    public int top() {
        int current = 0;
        if(head != null){
            current = head.getCurrentValue();
        }
        return current;
    }

    public int getMin() {
        int min = 0;
        if(head != null){
            min = head.getMinValue();
        }
        return min;
    }
}

class Element {
    private int currentValue;
    private int minValue;

    public Element next;

    public Element(int cValue, int mValue){
        this.currentValue = cValue;
        this.minValue = mValue;
    }
    public int getCurrentValue(){
        return this.currentValue;
    }
    public void setCurrentValue(int value){
        this.currentValue = value;
    }
    public int getMinValue(){
        return this.minValue;
    }
    public void setMinValue(int value){
        this.minValue = value;
    }
}

