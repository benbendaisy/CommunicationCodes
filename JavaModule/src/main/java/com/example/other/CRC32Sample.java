package com.example.other;

import java.util.zip.CRC32;
import java.util.zip.Checksum;

/**
 * Created by benbendaisy on 4/25/15.
 */
public class CRC32Sample {
    public static void main(String[] args) {
        String input = "Java Code Geeks - Java Examples";
        byte[] bytes = input.getBytes();
        Checksum checksum = new CRC32();
        checksum.update(bytes, 0, bytes.length);
        long checksumValue = checksum.getValue();
        System.out.println(checksumValue);
    }
}
