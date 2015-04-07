package com.example.other;//
//  Main.java
//  codescreen

//import src.*;

public class Main {
    private static final RangeModule rangeModule = new RangeModule();
    public static void main(String[] args) {
        Main main = new Main();
        main.testInsert();
        main.testInsertDuplicate();
        main.testRangeQuery();
        main.testDelete();
        main.testNonExistRangeDelete();

    }

    public void testInsert() {
        rangeModule.AddRange(1, 2);
        rangeModule.printAll();
        rangeModule.AddRange(2, 3);
        rangeModule.printAll();
    }

    public void testInsertDuplicate() {
        rangeModule.AddRange(1, 2);
        rangeModule.printAll();
    }

    public void testRangeQuery() {
        System.out.println(rangeModule.QueryRange(1, 2));
        System.out.println(rangeModule.QueryRange(1, 3));
        System.out.println(rangeModule.QueryRange(2, 3));
        System.out.println(rangeModule.QueryRange(1, 1));
        System.out.println(rangeModule.QueryRange(3, 3));
        System.out.println(rangeModule.QueryRange(0, 1));
        System.out.println(rangeModule.QueryRange(3, 5));

    }

    public void testDelete() {
        rangeModule.DeleteRange(1, 2);
        rangeModule.printAll();
    }

    public void testNonExistRangeDelete() {
        rangeModule.DeleteRange(1, 3);
        rangeModule.printAll();
    }

}