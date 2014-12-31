package com.example.lee;

/**
 * Created by benbendaisy on 12/21/14.
 * Given a positive integer, return its corresponding column title as appear in an Excel sheet.
 * For example:
 * 1 -> A
 * 2 -> B
 * 3 -> C
 ...
 * 26 -> Z
 * 27 -> AA
 * 28 -> AB
 */
public class ExcelSheetColumnTitle {
    public String convertToTitle(int n) {

        if(n < 1){
            return "" + n;
        }

        StringBuilder sb = new StringBuilder();
        int remainer = 0;
        while(n > 0){
            remainer = n % 26;
            n = (n-1)/26;
            if(remainer == 0){
                sb.append('Z');
            } else {
                sb.append((char) (remainer - 1 + 'A'));
            }
        }

        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        ExcelSheetColumnTitle excelSheetColumnTitle = new ExcelSheetColumnTitle();
        System.out.println(excelSheetColumnTitle.convertToTitle(1000000001));
    }
}
