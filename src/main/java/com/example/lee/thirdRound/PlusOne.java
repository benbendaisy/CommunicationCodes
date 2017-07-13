package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/12/17.
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {
        if (digits == null || digits.length == 0) {
            return digits;
        }

        int carrier = 0, idx = digits.length - 1;
        while (idx >= 0) {
            int sum = digits[idx] + carrier;
            if (idx == digits.length - 1) {
                sum += 1;
            }
            digits[idx] = sum % 10;
            carrier = sum / 10;
            idx--;
        }

        if (idx < 0 && carrier != 0) {
            int[] newArray = new int[digits.length + 1];
            newArray[0] = carrier;
            for (int i = 0; i < digits.length; i++) {
                newArray[i + 1] = digits[i];
            }
            return newArray;
        }

        return digits;
    }

    public static void main(String[] args) {
        PlusOne plusOne = new PlusOne();
        int[] digits = {9};
        System.out.println(plusOne.plusOne(digits));
    }
}
