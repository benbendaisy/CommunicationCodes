package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 12/29/14.
 * Related to question Excel Sheet Column Title
 * Given a column title as appear in an Excel sheet, return its corresponding column number.
 * For example:
 * A -> 1
 * B -> 2
 * C -> 3
 ...
 * Z -> 26
 * AA -> 27
 * AB -> 28
 */
public class ExcelSheetColumnNumber {
    public int titleToNumber(String s) {
        if(s == null || s.length() == 0){
            return 0;
        }

        int len = s.length();
        int num = 0;
        for(int i = 0; i < len; i++){
            num = num * 26 + s.charAt(i) - 'A' + 1;
        }
        return num;
    }
}
