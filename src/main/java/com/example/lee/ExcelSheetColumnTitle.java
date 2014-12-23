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

        while(n > 26){
            sb.append('A');
            n -= 26;
        }

        if(n > 0){
            sb.append((char) (n - 1 + 'A'));
        }

        return sb.toString();
    }

    public String convertToTitle1(int n) {
        if(n < 1){
            return "" + n;
        }

        StringBuilder sb = new StringBuilder();

        int countA = n / 26;
        int remainer = n % 26;

        for(int i = 0; i < countA; i++){
            sb.append("A");
        }

        if(remainer > 0){
            sb.append((char) (remainer - 1 + 'A'));
        }

        return sb.toString();
    }

    public String convertToTitle3(int n) {
        if(n < 1){
            return "" + n;
        }

        //StringBuilder sb = new StringBuilder();
        String result = "";
        int countA = n / 26;
        int remainer = n % 26;

        for(int i = 0; i < countA; i++){
            result = result + 'A';
        }

        if(remainer > 0){
            result = result + (char) (remainer - 1 + 'A');
        }

        return result;
    }

    public String convertToTitle2(int n) {
        StringBuffer s= new StringBuffer();

        while(n > 26){
            s.append('A');
            n -= 26;
        }

        if(n > 0){
            s.append((char)('A'+ n - 1));
        }

        return s.toString();
    }

    public static void main(String[] args) {
        ExcelSheetColumnTitle excelSheetColumnTitle = new ExcelSheetColumnTitle();
        System.out.println(excelSheetColumnTitle.convertToTitle1(1000000001));
    }
}
