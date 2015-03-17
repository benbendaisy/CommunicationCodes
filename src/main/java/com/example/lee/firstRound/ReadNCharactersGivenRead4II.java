package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/15/15.
 *
 * The API: int read4(char *buf) reads 4 characters at a time from a file.
 *
 * The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
 *
 * By using the read4 API, implement the function int read(char *buf, int n) that reads
 * n characters from the file.
 *
 * Note:
 *
 * The read function may be called multiple times.
 */

//refer to http://www.danielbit.com/blog/puzzle/leetcode/leetcode-read-n-characters-given-read4-ii
public class ReadNCharactersGivenRead4II {
    int offset = 0, bufLeft = 0;
    private char[] buffer = new char[4];
    private int readBytes = 0;
    private int read4(char[] buffer){
        return 0;
    }
    public int read(char[] buf, int n) {
        boolean eof = false;
        while (!eof && readBytes < n) {
            int s = (bufLeft > 0) ? bufLeft : read4(buffer);
            if (bufLeft == 0 && s < 4) {
                eof = true;
            }
            int realBytes = Math.min(n - readBytes, s);
            System.arraycopy(buffer /* src */, offset /* srcPos */, buf /* dest */, readBytes /* destPos */, realBytes /* length */);
            offset = (offset + realBytes) % 4;
            bufLeft = s - realBytes;
        }
        return readBytes;
    }
}
