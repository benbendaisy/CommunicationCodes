package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/12/17.
 */
public class AddBinary {
    public String addBinary(String a, String b) {
        if (a == null || b == null || a.length() == 0 || b.length() == 0) {
            return "";
        }

        int idxa = a.length() - 1, idxb = b.length() - 1;
        int carrier = 0;
        StringBuilder sb = new StringBuilder();
        while (idxa >= 0 && idxb >= 0) {
            int sum = (a.charAt(idxa) - '0') + (b.charAt(idxb) - '0') + carrier;
            sb.insert(0, sum % 2);
            carrier = sum / 2;
            idxa--;
            idxb--;
        }

        while (idxa >= 0) {
            int sum = (a.charAt(idxa) - '0') + carrier;
            sb.insert(0, sum % 2);
            carrier = sum / 2;
            idxa--;
        }

        while (idxb >= 0) {
            int sum = (b.charAt(idxb) - '0') + carrier;
            sb.insert(0, sum % 2);
            carrier = sum / 2;
            idxb--;
        }

        if (carrier != 0) {
            sb.insert(0, carrier);
        }

        return sb.toString();
    }
}
