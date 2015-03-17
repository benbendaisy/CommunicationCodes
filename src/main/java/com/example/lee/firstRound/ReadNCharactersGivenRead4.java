package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/8/15.
 */
public class ReadNCharactersGivenRead4 {
    private int read4(char[] buffer){
        return 0;
    }
    public int read(char[] buf, int n) {

        char[] buffer = new char[4];
        boolean endOfFile = false;
        int readBytes = 0;

        while (readBytes < n && !endOfFile) {
            int currReadBytes = read4(buffer);
            if (currReadBytes != 4) {
                endOfFile = true;
            }
            int length = Math.min(n - readBytes, currReadBytes);
            for (int i = 0; i < length; i++) {
                buf[readBytes + i] = buffer[i];
            }
            readBytes += length;
        }
        return readBytes;
    }


    //my version
    public int readI(char[] buf, int n) {
        if(buf == null || buf.length < n){
            return -1;
        }

        boolean isEnd = false;
        int readBytes = 0;
        char[] buffer = new char[4];
        while (readBytes < n && !isEnd) {
            int read4length = read4(buffer);
            if(read4length != 4){
                isEnd = true;
            }

            //find the real length that needed. This is for last time
            int length = Math.min(n - readBytes, read4length);
            for(int i = 0; i < length; i++){
                buf[readBytes + i] = buffer[i];
            }

            //adding real length
            readBytes += length;
        }
        return readBytes;
    }

    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */

    //refer to http://www.danielbit.com/blog/puzzle/leetcode/leetcode-read-n-characters-given-read4
    public int readII(char[] buf, int n) {
        char[] buffer = new char[4];
        int readBytes = 0;
        boolean eof = false;
        while (!eof && readBytes < n) {
            int s = read4(buffer);
            if (s < 4) {
                eof = true;
            }
            int realBytes = Math.min(n - readBytes, s);
            System.arraycopy(buffer /* src */, 0 /* srcPos */, buf /* dest */, readBytes /* destPos */, realBytes /* length */);
            //System.arraycopy(buffer, readBytes, buf, readBytes, realBytes);
            readBytes += realBytes;
        }
        return readBytes;
    }

}
