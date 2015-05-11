package com.example.syntax;

import java.util.UUID;

/**
 * Created by pzhong1 on 5/9/15.
 */
public class UUIDDemo {
    public static void main(String[] args) {
        // creating UUID
        UUID uid = UUID.fromString("38400000-8cf0-11bd-b23e-10b96e4ef00d");

        // checking the value of random UUID
        System.out.println("Random UUID value: "+uid.randomUUID());
    }
}
