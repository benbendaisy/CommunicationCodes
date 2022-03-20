package com.example.syntax;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;

/**
 * Created by pzhong1 on 4/29/15.
 *
 * refer to http://www.cnblogs.com/jxlgetter/p/4395098.html
 */
public class TextFileBufferedReader implements Iterable<String> {
    private BufferedReader br;

    public TextFileBufferedReader(String fileName) throws FileNotFoundException {
        br = new BufferedReader(new FileReader(fileName));
    }

    @Override
    public Iterator<String> iterator() {
        return new Iterator<String>() {
            @Override
            public boolean hasNext() {
                try {
                    br.mark(1);
                    if (br.read() < 0) {
                        return false;
                    }
                    br.reset();
                    return true;
                } catch (IOException e) {
                    return false;
                }
            }

            @Override
            public String next() {
                try {
                    return br.readLine();
                } catch (IOException e) {
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
