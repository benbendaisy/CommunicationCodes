package com.example.syntax;


import java.io.*;

/**
 * Created by pzhong1 on 4/29/15.
 */

public class ReverseLineInputStream extends InputStream {

    RandomAccessFile in;

    long currentLineStart = -1;
    long currentLineEnd = -1;
    long currentPos = -1;
    long lastPosInFile = -1;
    int lastChar = -1;

    public ReverseLineInputStream(File file) throws FileNotFoundException {
        in = new RandomAccessFile(file, "r");
        currentLineStart = file.length();
        currentLineEnd = file.length();
        lastPosInFile = file.length() -1;
        currentPos = currentLineEnd;

    }

    private void findPrevLine() throws IOException {
        if (lastChar == -1) {
            in.seek(lastPosInFile);
            lastChar = in.readByte();
        }

        currentLineEnd = currentLineStart;

        // There are no more lines, since we are at the beginning of the file and no lines.
        if (currentLineEnd == 0) {
            currentLineEnd = -1;
            currentLineStart = -1;
            currentPos = -1;
            return;
        }

        long filePointer = currentLineStart -1;

        while ( true) {
            filePointer--;

            // we are at start of file so this is the first line in the file.
            if (filePointer < 0) {
                break;
            }

            in.seek(filePointer);
            int readByte = in.readByte();

            // We ignore last LF in file. search back to find the previous LF.
            if (readByte == 0xA && filePointer != lastPosInFile ) {
                break;
            }
        }
        // we want to start at pointer +1 so we are after the LF we found or at 0 the start of the file.
        currentLineStart = filePointer + 1;
        currentPos = currentLineStart;
    }

    public int read() throws IOException {

        if (currentPos < currentLineEnd ) {
            in.seek(currentPos++);
            int readByte = in.readByte();
            return readByte;
        } else if (currentPos > lastPosInFile && currentLineStart < currentLineEnd) {
            // last line in file (first returned)
            findPrevLine();
            if (lastChar != '\n' && lastChar != '\r') {
                // last line is not terminated
                return '\n';
            } else {
                return read();
            }
        } else if (currentPos < 0) {
            return -1;
        } else {
            findPrevLine();
            return read();
        }
    }

    @Override
    public void close() throws IOException {
        if (in != null) {
            in.close();
            in = null;
        }
    }

    public static void main(String[] args) {
        BufferedReader in = null;
        try {
            in = new BufferedReader (new InputStreamReader (new ReverseLineInputStream(new File("xyz.txt"))));
            String line;
            while((line = in.readLine()) != null) {
                System.out.println("X:" + line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (null != in) {
                try {
                    in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}