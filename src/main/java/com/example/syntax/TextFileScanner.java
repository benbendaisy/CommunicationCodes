package com.example.syntax;

import java.io.File;
import java.util.Iterator;
import java.util.Scanner;

/**
 * Created by benbendaisy on 4/29/15.
 */
public class TextFileScanner implements Iterable<String> {
    Scanner scanner;
    public TextFileScanner(String fileName) {
        try {
            scanner = new Scanner(new File(fileName));
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    public Iterator<String> iterator() {
        return new Iterator<String>() {
            @Override
            public boolean hasNext() {
                return scanner.hasNext();
            }
            @Override
            public String next() {
                if (hasNext()) {
                    return scanner.nextLine();
                } else {
                    return null;
                }
            }
            @Override
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }
}
