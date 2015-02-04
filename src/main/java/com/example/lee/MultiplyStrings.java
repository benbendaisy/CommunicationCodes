package com.example.lee;

/**
 * Created by benbendaisy on 2/3/15.
 */
public class MultiplyStrings {
    public String multiply(String num1, String num2) {
        if(null == num1 || null == num2){
            return null;
        } else if("0".equals(num1) || "0".equals(num2)){
            return "0";
        }
        int idx1 = num1.length() - 1, carr = 0;
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        while(idx1 >= 0){
            int i1 = num1.charAt(idx1) - '0';
            int idx2 = num2.length() - 1;
            int lidx = idx;
            while(idx2 >= 0){
                int i2 = num2.charAt(idx2) - '0';
                int m = i1 * i2 + carr;
                if(sb.length() > lidx){
                    m += sb.charAt(lidx) - '0';
                }
                int r = m % 10;
                carr = m / 10;
                if(sb.length() > lidx){
                    sb.setCharAt(lidx, Character.forDigit(r, 10));
                } else {
                    sb.append(r);
                }
                lidx++;
                idx2--;
            }
            if(carr != 0){
                sb.append(carr);
                carr = 0;
            }
            idx1--;
            idx++;
        }

        if(carr != 0){
            sb.append(carr);
        }

        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        MultiplyStrings multiplyStrings = new MultiplyStrings();
        System.out.println(multiplyStrings.multiply("123", "456"));
    }
}
