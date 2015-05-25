package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/16/15.
 */
public class AddBinary {
    public String addBinary(String a, String b) {
        if (null == a && null == b) {
            return null;
        } else if (null == a || a.length() == 0) {
            return b;
        } else if (null == b || b.length() == 0) {
            return a;
        }

        int idxa = a.length() - 1, idxb = b.length() - 1;
        int crr = 0;
        StringBuilder sb = new StringBuilder();
        while (idxa >= 0 && idxb >= 0) {
            int ia = a.charAt(idxa) - '0';
            int ib = b.charAt(idxb) - '0';
            int sum = ia + ib + crr;
            sb.insert(0, sum % 2);
            crr = sum / 2;
            idxa--;
            idxb--;
        }

        while (idxa >= 0) {
            int ia = a.charAt(idxa) - '0';
            int sum = ia + crr;
            sb.insert(0, sum % 2);
            crr = sum / 2;
            idxa--;
        }

        while (idxb >= 0) {
            int ib = b.charAt(idxb) - '0';
            int sum = ib + crr;
            sb.insert(0, sum % 2);
            crr = sum / 2;
            idxb--;
        }

        if (crr != 0) sb.insert(0, crr);

        return sb.toString();
    }

    public static void main(String[] args) {
        AddBinary addBinary = new AddBinary();
        System.out.println(addBinary.addBinary("11", "1"));
    }
}
