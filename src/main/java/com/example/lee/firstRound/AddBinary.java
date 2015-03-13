package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/19/15.
 * Given two binary strings, return their sum (also a binary string).
 *
 * For example,
 * a = "11"
 * b = "1"
 * Return "100".
 */
public class AddBinary {
    public String addBinary(String a, String b) {
        if(a == null || b == null){
            return null;
        } else if (a.isEmpty()) {
            return b;
        } else if (b.isEmpty()){
            return a;
        }
        int right1 = a.length() - 1, right2 = b.length() - 1;
        int c = 0;
        StringBuilder sb = new StringBuilder();
        while(right1 >= 0 && right2 >= 0){
            int current = 0;
            if(a.charAt(right1) == '1' && b.charAt(right2) == '1'){
                current = 2;
            } else if(a.charAt(right1) == '1' || b.charAt(right2) == '1'){
                current = 1;
            } else{
                current = 0;
            }
            current += c;
            switch (current){
                case 0: sb.insert(0, '0'); c = 0; break;
                case 1: sb.insert(0, '1'); c = 0; break;
                case 2: sb.insert(0, '0'); c = 1; break;
                case 3: sb.insert(0, '1'); c = 1; break;
            }
            right1--;
            right2--;
        }

        while(right1 >= 0){
            int current = 0;
            if(a.charAt(right1) == '1'){
                current = 1;
            } else{
                current = 0;
            }
            current += c;
            switch (current){
                case 0: sb.insert(0, '0'); c = 0; break;
                case 1: sb.insert(0, '1'); c = 0; break;
                case 2: sb.insert(0, '0'); c = 1; break;
            }
            right1--;
        }

        while(right2 >= 0){
            int current = 0;
            if(b.charAt(right2) == '1'){
                current = 1;
            } else{
                current = 0;
            }
            current += c;
            switch (current){
                case 0: sb.insert(0, '0'); c = 0; break;
                case 1: sb.insert(0, '1'); c = 0; break;
                case 2: sb.insert(0, '0'); c = 1; break;
            }
            right2--;
        }

        if(c > 0){
            sb.insert(0, c);
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        AddBinary addBinary = new AddBinary();
        System.out.println(addBinary.addBinary("1", "1"));
    }
}
