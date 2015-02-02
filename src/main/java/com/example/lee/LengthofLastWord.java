package com.example.lee;

/**
 * Created by benbendaisy on 1/23/15.
 * Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
 *
 * If the last word does not exist, return 0.
 *
 * Note: A word is defined as a character sequence consists of non-space characters only.
 *
 * For example,
 * Given s = "Hello World",
 * return 5.
 */
public class LengthofLastWord {
    public int lengthOfLastWord(String s) {
        if(s == null || s.length() == 0 || s.trim().length() == 0){
            return 0;
        }
        String str = s.trim();
        int i = str.length() - 1;
        while(i >= 0){
            if(' ' != str.charAt(i)){
                i--;
            } else {
                break;
            }
        }
        return str.length() - i - 1;
    }

    public static void main(String[] args) {
        LengthofLastWord lengthofLastWord = new LengthofLastWord();
        System.out.println(lengthofLastWord.lengthOfLastWord("     "));
    }
}
