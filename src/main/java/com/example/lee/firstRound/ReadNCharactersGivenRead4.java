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
            if (currReadBytes !=4) {
                endOfFile = true;
            }
            int length = Math.min(n - readBytes, currReadBytes);
            for (int i=0; i<length; i++) {
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

}
