package com.example.lee;

/**
 * Created by benbendaisy on 1/19/15.
 *
 * Given a non-negative number represented as an array of digits, plus one to the number.
 *
 * The digits are stored such that the most significant digit is at the head of the list.
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {
        if(digits == null){
            return null;
        }
        int c = 1;
        for(int i = digits.length - 1; i >= 0; i--){
            digits[i] += c;
            if(digits[i] >= 10){
                digits[i] -= 10;
                c = 1;
            } else {
                c = 0;
            }
        }
        if(c > 0){
            int[] newArray = new int[digits.length + 1];
            for(int i = 1; i < newArray.length; i++){
                newArray[i] = digits[i - 1];
            }
            newArray[0] = c;
            return newArray;
        }
        return digits;
    }

    public static void main(String[] args) {
        PlusOne plusOne = new PlusOne();
        int[] digits = {0};
        int[] number = plusOne.plusOne(digits);
        for(int i : number){
            System.out.println(i);
        }
    }
}
