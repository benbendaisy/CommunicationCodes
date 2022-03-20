package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/9/17.
 */
public class LengthofLastWord {
    public int lengthOfLastWord(String s) {
        if (s == null || s.length() < 1) {
            return 0;
        }
        String trimmedStr = s.trim();
        if (trimmedStr.length() == 0) {
            return 0;
        }
        String[] fields = trimmedStr.split(" ");
        if (fields == null || fields.length < 1) {
            return 0;
        }
        String lastWord = fields[fields.length - 1];
        return lastWord.length();
    }

    public static void main(String[] args) {
        LengthofLastWord lengthofLastWord = new LengthofLastWord();
        System.out.println(lengthofLastWord.lengthOfLastWord(" "));
    }
}
